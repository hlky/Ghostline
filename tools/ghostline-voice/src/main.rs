//! Ghostline voice authoring command-line interface.

use std::collections::{BTreeMap, BTreeSet};
use std::path::{Path, PathBuf};

use clap::{Args, Parser, Subcommand, ValueEnum};
use dinoml_qwen3_tts::{GenerationSamplingConfig, SamplingConfig};
use dinoml_runtime::Device;
use ghostline_voice::cr2w::{LocalizationTemplates, serialize_all};
use ghostline_voice::embedding::convert_embedding;
use ghostline_voice::local::{LocalDinoMlBackend, LocalDinoMlConfig};
use ghostline_voice::localization::generate_all;
use ghostline_voice::manifest::VoicePlan;
use ghostline_voice::render::{RenderOptions, render_plan};
use ghostline_voice::{Error, Result};
use serde_json::json;

const DEFAULT_INDEX: &str = "quests/story/ghostline/gq003/script/voice-production.json";

#[derive(Debug, Parser)]
#[command(about = "Ghostline voice and localization authoring pipeline")]
struct Cli {
    #[command(subcommand)]
    command: Command,
}

#[derive(Debug, Subcommand)]
enum Command {
    /// Validate the production index and every dialogue manifest.
    Validate(PlanArgs),
    /// Convert a canonical or `DinoML` speaker embedding to `DinoML` JSON.
    ConvertEmbedding {
        /// Source `.safetensors` or `DinoML` `.json` embedding.
        input: PathBuf,
        /// Destination `DinoML` JSON asset.
        output: PathBuf,
    },
    /// Regenerate subtitle, subtitle-map, and VO-map CR2W-JSON.
    Localize(PlanArgs),
    /// Serialize and round-trip verify every localization CR2W resource.
    Serialize(SerializeArgs),
    /// Render deterministic audition candidates through a persistent local model.
    RenderLocal(RenderLocalArgs),
}

#[derive(Debug, Clone, Args)]
struct PlanArgs {
    /// Ghostline repository root.
    #[arg(long, default_value = ".")]
    repo_root: PathBuf,
    /// Voice-production index, relative to the repository root by default.
    #[arg(long, default_value = DEFAULT_INDEX)]
    index: PathBuf,
}

#[derive(Debug, Args)]
struct SerializeArgs {
    #[command(flatten)]
    plan: PlanArgs,
    /// RED reflection schema.
    #[arg(long, default_value = "red-schema.json")]
    schema: PathBuf,
    /// Compatible subtitle-entry CR2W template.
    #[arg(
        long,
        default_value = "source/archive/mod/gq003/localization/en-us/subtitles/gq003_17.json"
    )]
    subtitles_template: PathBuf,
    /// Compatible subtitle-map CR2W template.
    #[arg(
        long,
        default_value = "source/archive/mod/gq000/localization/en-us/subtitles/gq000_01_subtitles_map.json"
    )]
    subtitle_map_template: PathBuf,
    /// Compatible VO-map CR2W template.
    #[arg(
        long,
        default_value = "source/archive/mod/gq003/localization/en-us/vo/gq003_17.json"
    )]
    voiceover_map_template: PathBuf,
}

#[derive(Debug, Args)]
struct RenderLocalArgs {
    #[command(flatten)]
    plan: PlanArgs,
    /// Qwen3-TTS Base checkpoint directory.
    #[arg(long)]
    checkpoint: PathBuf,
    /// Compiled Base generation artifact directory.
    #[arg(long)]
    generation_artifact: PathBuf,
    /// Compiled tokenizer decoder artifact directory.
    #[arg(long)]
    decoder_artifact: PathBuf,
    /// Candidate output root.
    #[arg(long, default_value = "generated-voices/gq003")]
    output: PathBuf,
    /// Limit rendering to one or more dialogue IDs.
    #[arg(long)]
    dialogue: Vec<String>,
    /// Speaker embedding override formatted as `NAME=PATH`.
    #[arg(long = "embedding", value_parser = parse_embedding_override)]
    embeddings: Vec<(String, PathBuf)>,
    /// Number of deterministic candidates per line.
    #[arg(long, default_value_t = 3)]
    versions: u32,
    /// Stable seed namespace.
    #[arg(long, default_value_t = 3_000)]
    seed_base: u64,
    /// Prompt language.
    #[arg(long, default_value = "English")]
    language: String,
    /// Maximum generated codec frames.
    #[arg(long, default_value_t = 240)]
    max_frames: usize,
    /// Outer-talker temperature.
    #[arg(long, default_value_t = 0.95)]
    temperature: f32,
    /// Outer-talker top-k; must match the compiled artifact policy.
    #[arg(long, default_value_t = 50)]
    top_k: usize,
    /// Outer-talker nucleus probability.
    #[arg(long, default_value_t = 0.98)]
    top_p: f32,
    /// Outer-talker repetition penalty.
    #[arg(long, default_value_t = 1.0)]
    repetition_penalty: f32,
    /// Code-predictor temperature.
    #[arg(long, default_value_t = 0.9)]
    subtalker_temperature: f32,
    /// Code-predictor top-k; must match the compiled artifact policy.
    #[arg(long, default_value_t = 50)]
    subtalker_top_k: usize,
    /// Code-predictor nucleus probability.
    #[arg(long, default_value_t = 1.0)]
    subtalker_top_p: f32,
    /// Runtime execution device.
    #[arg(long, value_enum, default_value_t = ExecutionDevice::Rocm)]
    device: ExecutionDevice,
    /// Zero-based runtime device index.
    #[arg(long, default_value_t = 0)]
    device_index: u32,
    /// Enable artifact graph replay.
    #[arg(long)]
    graph_replay: bool,
    /// Replace stale existing candidates.
    #[arg(long)]
    force: bool,
}

#[derive(Debug, Clone, Copy, ValueEnum)]
enum ExecutionDevice {
    Cpu,
    Rocm,
    Cuda,
}

impl ExecutionDevice {
    const fn resolve(self, index: u32) -> Device {
        match self {
            Self::Cpu => Device::cpu(),
            Self::Rocm => Device::rocm(index),
            Self::Cuda => Device::cuda(index),
        }
    }
}

fn main() -> Result<()> {
    match Cli::parse().command {
        Command::Validate(args) => {
            let plan = load_plan(&args)?;
            print_json(&json!({
                "ok": true,
                "quest": plan.production.quest,
                "dialogues": plan.dialogues.len(),
                "spoken_lines": plan.production.spoken_line_count,
            }))?;
        }
        Command::ConvertEmbedding { input, output } => {
            convert_embedding(&input, &output)?;
            print_json(&json!({"input": input, "output": output}))?;
        }
        Command::Localize(args) => {
            let plan = load_plan(&args)?;
            let outputs = generate_all(&plan)?;
            print_json(&json!({
                "quest": plan.production.quest,
                "dialogues": outputs.len(),
                "resources": outputs.len() * 3,
            }))?;
        }
        Command::Serialize(args) => {
            let plan = load_plan(&args.plan)?;
            let schema = resolve(&plan.repo_root, &args.schema);
            let templates = LocalizationTemplates {
                subtitles: resolve(&plan.repo_root, &args.subtitles_template),
                subtitle_map: resolve(&plan.repo_root, &args.subtitle_map_template),
                voiceover_map: resolve(&plan.repo_root, &args.voiceover_map_template),
            };
            let outputs = serialize_all(&plan, schema, &templates)?;
            print_json(&json!({
                "quest": plan.production.quest,
                "resources": outputs,
            }))?;
        }
        Command::RenderLocal(args) => render_local(&args)?,
    }
    Ok(())
}

fn render_local(args: &RenderLocalArgs) -> Result<()> {
    let plan = load_plan(&args.plan)?;
    let outer = SamplingConfig::new(
        true,
        args.temperature,
        args.top_k,
        args.top_p,
        args.repetition_penalty,
    )?;
    let code_predictor = SamplingConfig::new(
        true,
        args.subtalker_temperature,
        args.subtalker_top_k,
        args.subtalker_top_p,
        1.0,
    )?;
    let mut config = LocalDinoMlConfig::new(
        resolve(&plan.repo_root, &args.checkpoint),
        resolve(&plan.repo_root, &args.generation_artifact),
        resolve(&plan.repo_root, &args.decoder_artifact),
        args.device.resolve(args.device_index),
    );
    config.graph_replay = args.graph_replay;
    // SAFETY: RenderLocal is an explicit request to execute the supplied
    // checkpoint artifact libraries in-process. The command documents and
    // preserves DinoML's trusted-artifact boundary.
    let mut backend = unsafe { LocalDinoMlBackend::load(&config) }?;
    if args.max_frames > backend.frame_capacity() {
        return Err(Error::manifest(format!(
            "requested {} frames but the generation artifact supports at most {}",
            args.max_frames,
            backend.frame_capacity()
        )));
    }
    let options = RenderOptions {
        output_root: resolve(&plan.repo_root, &args.output),
        dialogues: args.dialogue.iter().cloned().collect::<BTreeSet<_>>(),
        speaker_embeddings: args.embeddings.iter().cloned().collect::<BTreeMap<_, _>>(),
        versions: args.versions,
        seed_base: args.seed_base,
        language: args.language.clone(),
        max_frames: args.max_frames,
        sampling: GenerationSamplingConfig::new(outer, code_predictor),
        force: args.force,
    };
    let report = render_plan(&plan, &mut backend, &options)?;
    print_json(&json!({
        "quest": report.quest,
        "candidates": report.candidates.len(),
        "output": options.output_root,
    }))
}

fn load_plan(args: &PlanArgs) -> Result<VoicePlan> {
    VoicePlan::load(&args.repo_root, &args.index)
}

fn resolve(root: &Path, path: &Path) -> PathBuf {
    if path.is_absolute() {
        path.to_owned()
    } else {
        root.join(path)
    }
}

fn parse_embedding_override(value: &str) -> std::result::Result<(String, PathBuf), String> {
    let (speaker, path) = value
        .split_once('=')
        .ok_or_else(|| "expected NAME=PATH".to_owned())?;
    if speaker.trim().is_empty() || path.trim().is_empty() {
        return Err("expected nonempty NAME=PATH".to_owned());
    }
    Ok((speaker.to_owned(), PathBuf::from(path)))
}

fn print_json(value: &serde_json::Value) -> Result<()> {
    let encoded = serde_json::to_string_pretty(value)
        .map_err(|source| Error::json("standard output", source))?;
    println!("{encoded}");
    Ok(())
}
