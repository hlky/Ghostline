//! Ghostline voice authoring command-line interface.

#[cfg(feature = "render-local")]
use std::collections::{BTreeMap, BTreeSet};
use std::path::{Path, PathBuf};

#[cfg(feature = "render-local")]
use clap::ValueEnum;
use clap::{Args, Parser, Subcommand};
#[cfg(feature = "render-local")]
use dinoml_qwen3_tts::{GenerationSamplingConfig, SamplingConfig};
#[cfg(feature = "render-local")]
use dinoml_runtime::Device;
use ghostline_voice::cr2w::{LocalizationTemplates, serialize_all};
#[cfg(feature = "render-local")]
use ghostline_voice::embedding::convert_embedding;
#[cfg(feature = "render-local")]
use ghostline_voice::local::{LocalDinoMlBackend, LocalDinoMlConfig};
use ghostline_voice::localization::generate_all;
use ghostline_voice::manifest::VoicePlan;
#[cfg(feature = "render-local")]
use ghostline_voice::render::{RenderOptions, render_plan};
use ghostline_voice::{Error, Result};
use serde_json::json;

const DEFAULT_INDEX: &str = "projects/ghostline/quests/gq003/script/voice-production.json";

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
    #[cfg(feature = "render-local")]
    ConvertEmbedding {
        /// Source `.safetensors` or `DinoML` `.json` embedding.
        input: PathBuf,
        /// Destination `DinoML` JSON asset.
        output: PathBuf,
    },
    /// Encode a reference WAV/FLAC into full acoustic conditioning codes.
    #[cfg(feature = "render-local")]
    EncodeReference(EncodeReferenceArgs),
    /// Design a custom character reference WAV before full-reference cloning.
    #[cfg(feature = "render-local")]
    DesignReference(DesignReferenceArgs),
    /// Extract a speaker embedding from reference WAV/FLAC audio.
    #[cfg(feature = "render-local")]
    ExtractEmbedding {
        /// Original Base checkpoint model.safetensors file.
        #[arg(long)]
        checkpoint: PathBuf,
        /// Trusted compiled speaker-encoder artifact directory.
        #[arg(long)]
        speaker_artifact: PathBuf,
        /// Reference WAV or FLAC file.
        #[arg(long)]
        reference: PathBuf,
        /// Destination canonical .safetensors embedding.
        #[arg(long)]
        output: PathBuf,
        #[arg(long, value_enum, default_value_t = ExecutionDevice::Rocm)]
        device: ExecutionDevice,
        #[arg(long, default_value_t = 0)]
        device_index: u32,
    },
    /// Extract multiple references through one resident speaker encoder.
    #[cfg(feature = "render-local")]
    ExtractEmbeddings {
        /// Original Base checkpoint model.safetensors file.
        #[arg(long)]
        checkpoint: PathBuf,
        /// Trusted compiled speaker-encoder artifact directory.
        #[arg(long)]
        speaker_artifact: PathBuf,
        /// Reference WAV or FLAC files with unique basenames.
        #[arg(long, required = true, num_args = 1..)]
        reference: Vec<PathBuf>,
        /// Directory receiving one canonical embedding per reference basename.
        #[arg(long)]
        output_dir: PathBuf,
        #[arg(long, value_enum, default_value_t = ExecutionDevice::Rocm)]
        device: ExecutionDevice,
        #[arg(long, default_value_t = 0)]
        device_index: u32,
    },
    /// Average multiple same-speaker embeddings without changing their scale.
    #[cfg(feature = "render-local")]
    MergeEmbeddings {
        /// Input canonical .safetensors or `DinoML` .json embeddings.
        #[arg(long, required = true, num_args = 1..)]
        input: Vec<PathBuf>,
        /// Destination canonical .safetensors embedding.
        #[arg(long)]
        output: PathBuf,
    },
    /// Regenerate subtitle, subtitle-map, and VO-map CR2W-JSON.
    Localize(PlanArgs),
    /// Generate localization for one manifest, including historical audio names.
    LocalizeManifest(LocalizeManifestArgs),
    /// Serialize and round-trip verify every localization CR2W resource.
    Serialize(SerializeArgs),
    /// Render deterministic audition candidates through a persistent local model.
    #[cfg(feature = "render-local")]
    RenderLocal(Box<RenderLocalArgs>),
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

#[cfg(feature = "render-local")]
#[derive(Debug, Args)]
struct EncodeReferenceArgs {
    /// Speech tokenizer model.safetensors file.
    #[arg(long)]
    checkpoint: PathBuf,
    /// Trusted tokenizer-encoder artifact covering the reference sample domain.
    #[arg(long)]
    encoder_artifact: PathBuf,
    #[arg(long)]
    reference: PathBuf,
    #[arg(long)]
    output: PathBuf,
    #[arg(long, value_enum, default_value_t = ExecutionDevice::Rocm)]
    device: ExecutionDevice,
    #[arg(long, default_value_t = 0)]
    device_index: u32,
}

#[cfg(feature = "render-local")]
#[derive(Debug, Args)]
struct DesignReferenceArgs {
    /// Original Qwen3-TTS `VoiceDesign` checkpoint directory.
    #[arg(long)]
    checkpoint: PathBuf,
    /// Trusted compiled `VoiceDesign` generation artifact.
    #[arg(long)]
    generation_artifact: PathBuf,
    /// Trusted compiled tokenizer decoder artifact.
    #[arg(long)]
    decoder_artifact: PathBuf,
    /// Exact words to speak in the reusable reference recording.
    #[arg(long)]
    text: String,
    /// Voice description, separate from the spoken words.
    #[arg(long)]
    instruction: String,
    #[arg(long, default_value = "English")]
    language: String,
    #[arg(long)]
    output: PathBuf,
    #[arg(long)]
    seed: u64,
    #[arg(long, default_value_t = 240)]
    max_frames: usize,
    #[arg(long, value_enum, default_value_t = ExecutionDevice::Rocm)]
    device: ExecutionDevice,
    #[arg(long, default_value_t = 0)]
    device_index: u32,
}

#[derive(Debug, Args)]
struct LocalizeManifestArgs {
    #[arg(long, default_value = ".")]
    repo_root: PathBuf,
    #[arg(long)]
    manifest: PathBuf,
    #[arg(long)]
    quest: String,
    #[arg(long)]
    dialogue: String,
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
        default_value = "projects/ghostline/source/archive/mod/gq003/localization/en-us/subtitles/gq003_17.json"
    )]
    subtitles_template: PathBuf,
    /// Compatible subtitle-map CR2W template.
    #[arg(
        long,
        default_value = "projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us/subtitles/gq000_01_subtitles_map.json"
    )]
    subtitle_map_template: PathBuf,
    /// Compatible VO-map CR2W template.
    #[arg(
        long,
        default_value = "projects/ghostline/source/archive/mod/gq003/localization/en-us/vo/gq003_17.json"
    )]
    voiceover_map_template: PathBuf,
}

#[cfg(feature = "render-local")]
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
    /// Limit rendering to one or more speaker names.
    #[arg(long)]
    speaker: Vec<String>,
    /// Speaker embedding override formatted as `NAME=PATH`.
    #[arg(long = "embedding", value_parser = parse_embedding_override)]
    embeddings: Vec<(String, PathBuf)>,
    /// JSON speaker map of exact reference transcripts and codec assets.
    #[arg(long)]
    reference_prompts: Option<PathBuf>,
    /// Optional delivery instruction, separate from the words to speak.
    #[arg(long)]
    instruction: Option<String>,
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
    /// Rerender selected candidates, including valid existing outputs.
    #[arg(long)]
    force: bool,
}

#[cfg(feature = "render-local")]
#[derive(Debug, Clone, Copy, ValueEnum)]
enum ExecutionDevice {
    Cpu,
    Rocm,
    Cuda,
}

#[cfg(feature = "render-local")]
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
        #[cfg(feature = "render-local")]
        Command::EncodeReference(args) => encode_reference(&args)?,
        #[cfg(feature = "render-local")]
        Command::DesignReference(args) => design_reference(&args)?,
        Command::Validate(args) => {
            let plan = load_plan(&args)?;
            print_json(&json!({
                "ok": true,
                "quest": plan.production.quest,
                "dialogues": plan.dialogues.len(),
                "spoken_lines": plan.production.spoken_line_count,
            }))?;
        }
        #[cfg(feature = "render-local")]
        Command::ConvertEmbedding { input, output } => {
            convert_embedding(&input, &output)?;
            print_json(&json!({"input": input, "output": output}))?;
        }
        #[cfg(feature = "render-local")]
        Command::ExtractEmbedding {
            checkpoint,
            speaker_artifact,
            reference,
            output,
            device,
            device_index,
        } => {
            // SAFETY: This command explicitly requests execution of the supplied
            // trusted native speaker artifact, matching render-local's boundary.
            let mut encoder = unsafe {
                dinoml_qwen3_tts::SpeakerEncoderRunner::load(
                    &speaker_artifact,
                    &checkpoint,
                    device.resolve(device_index),
                )
            }?;
            let embedding = encoder.encode_path(&reference)?;
            ghostline_voice::embedding::save_embedding(&output, &embedding)?;
            print_json(
                &json!({"reference": reference, "output": output, "dimensions": embedding.len()}),
            )?;
        }
        #[cfg(feature = "render-local")]
        Command::ExtractEmbeddings {
            checkpoint,
            speaker_artifact,
            reference,
            output_dir,
            device,
            device_index,
        } => {
            extract_embedding_batch(
                &checkpoint,
                &speaker_artifact,
                &reference,
                &output_dir,
                device.resolve(device_index),
            )?;
        }
        #[cfg(feature = "render-local")]
        Command::MergeEmbeddings { input, output } => {
            merge_embeddings(&input, &output)?;
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
        Command::LocalizeManifest(args) => {
            let paths = ghostline_voice::localization::generate_manifest(
                &args.repo_root,
                &args.manifest,
                &args.quest,
                &args.dialogue,
            )?;
            print_json(
                &json!({"subtitles": paths.subtitle_raw, "voiceover_map": paths.voiceover_raw, "subtitle_map": paths.subtitle_map_raw}),
            )?;
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
        #[cfg(feature = "render-local")]
        Command::RenderLocal(args) => render_local(&args)?,
    }
    Ok(())
}

#[cfg(feature = "render-local")]
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
    config.instruction.clone_from(&args.instruction);
    if let Some(path) = &args.reference_prompts {
        config.references =
            ghostline_voice::local::load_reference_prompts(&resolve(&plan.repo_root, path))?;
        if config
            .references
            .keys()
            .any(|name| !plan.production.voice_sources.contains_key(name))
        {
            return Err(Error::manifest(
                "reference prompts contain an unknown performer",
            ));
        }
    }
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
        speakers: args.speaker.iter().cloned().collect::<BTreeSet<_>>(),
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

#[cfg(feature = "render-local")]
fn encode_reference(args: &EncodeReferenceArgs) -> Result<()> {
    // SAFETY: The user explicitly supplies this trusted native encoder artifact.
    let mut encoder = unsafe {
        dinoml_qwen3_tts::TokenizerEncoderRunner::load(
            &args.encoder_artifact,
            &args.checkpoint,
            args.device.resolve(args.device_index),
        )
    }?;
    let codes = encoder.encode_path(&args.reference)?;
    if let Some(parent) = args
        .output
        .parent()
        .filter(|parent| !parent.as_os_str().is_empty())
    {
        std::fs::create_dir_all(parent).map_err(|source| Error::io(parent, source))?;
    }
    dinoml_qwen3_tts::write_codec_frames(&args.output, &codes)?;
    print_json(
        &json!({"reference":args.reference,"output":args.output,"frames":codes.frame_count()}),
    )
}

#[cfg(feature = "render-local")]
fn design_reference(args: &DesignReferenceArgs) -> Result<()> {
    if args.text.trim().is_empty() || args.instruction.trim().is_empty() {
        return Err(Error::manifest(
            "reference text and voice instruction must be nonempty",
        ));
    }
    let builder = dinoml_qwen3_tts::PromptBuilder::load(&args.checkpoint)?;
    let prompt = builder.voice_design(&args.text, &args.instruction, &args.language)?;
    let aligned = builder.align(&prompt)?;
    // SAFETY: This command explicitly requests execution of both supplied
    // trusted native artifact libraries, matching render-local's boundary.
    let mut controller = unsafe {
        dinoml_qwen3_tts::SynthesisController::load(
            &args.checkpoint,
            &args.generation_artifact,
            &args.decoder_artifact,
            args.device.resolve(args.device_index),
        )
    }?;
    controller.set_graph_replay(false)?;
    let sampling = GenerationSamplingConfig::new(
        SamplingConfig::new(true, 0.95, 50, 0.98, 1.0)?,
        SamplingConfig::new(true, 0.9, 50, 1.0, 1.0)?,
    );
    let waveform =
        controller.synthesize_with_sampling(&aligned, args.max_frames, args.seed, sampling)?;
    if let Some(parent) = args.output.parent().filter(|p| !p.as_os_str().is_empty()) {
        std::fs::create_dir_all(parent).map_err(|source| Error::io(parent, source))?;
    }
    waveform.write_pcm16_wav(&args.output)?;
    dinoml_qwen3_tts::write_generation_record(&args.output, args.seed)?;
    print_json(
        &json!({"output":args.output,"seed":args.seed,"text":args.text,
        "instruction":args.instruction,"checkpoint":args.checkpoint,
        "generation_artifact":args.generation_artifact,"decoder_artifact":args.decoder_artifact,
        "status":"unreviewed_design_reference"}),
    )
}

#[cfg(feature = "render-local")]
fn merge_embeddings(input: &[PathBuf], output: &Path) -> Result<()> {
    let embeddings = input
        .iter()
        .map(ghostline_voice::embedding::load_embedding)
        .collect::<Result<Vec<_>>>()?;
    let merged = ghostline_voice::embedding::mean_embeddings(&embeddings)?;
    ghostline_voice::embedding::save_embedding(output, &merged)?;
    print_json(&json!({"inputs":input,"output":output,"dimensions":merged.len()}))
}

#[cfg(feature = "render-local")]
fn extract_embedding_batch(
    checkpoint: &Path,
    artifact: &Path,
    references: &[PathBuf],
    output_dir: &Path,
    device: Device,
) -> Result<()> {
    let mut names = BTreeSet::new();
    let mut outputs = Vec::with_capacity(references.len());
    for path in references {
        let name = path
            .file_stem()
            .ok_or_else(|| Error::manifest("reference has no basename"))?;
        let output = output_dir.join(name).with_extension("safetensors");
        if !names.insert(output.clone()) {
            return Err(Error::manifest(
                "batch references must have unique basenames",
            ));
        }
        outputs.push(output);
    }
    // SAFETY: This CLI operation explicitly supplies a trusted native artifact,
    // as with extract-embedding. One runner serves the complete batch.
    let mut encoder =
        unsafe { dinoml_qwen3_tts::SpeakerEncoderRunner::load(artifact, checkpoint, device) }?;
    let mut records = Vec::with_capacity(references.len());
    for (path, output) in references.iter().zip(outputs) {
        let embedding = encoder.encode_path(path)?;
        ghostline_voice::embedding::save_embedding(&output, &embedding)?;
        records.push(json!({"reference":path,"output":output,"dimensions":embedding.len()}));
    }
    print_json(&json!({"embeddings":records}))
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

#[cfg(feature = "render-local")]
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

#[cfg(all(test, feature = "render-local"))]
mod design_tests {
    use super::*;

    fn arguments(text: &str, instruction: &str) -> DesignReferenceArgs {
        DesignReferenceArgs {
            checkpoint: "missing-checkpoint".into(),
            generation_artifact: "missing-generation".into(),
            decoder_artifact: "missing-decoder".into(),
            text: text.into(),
            instruction: instruction.into(),
            language: "English".into(),
            output: "unused.wav".into(),
            seed: 4004,
            max_frames: 240,
            device: ExecutionDevice::Cpu,
            device_index: 0,
        }
    }

    #[test]
    fn empty_reference_text_is_rejected_before_loading_artifacts() {
        assert!(matches!(
            design_reference(&arguments(" ", "Warm conversational voice")),
            Err(Error::Manifest(_))
        ));
    }

    #[test]
    fn empty_voice_instruction_is_rejected_before_loading_artifacts() {
        assert!(matches!(
            design_reference(&arguments("Hello, V.", " ")),
            Err(Error::Manifest(_))
        ));
    }
}
