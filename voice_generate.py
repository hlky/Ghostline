import torch
from faster_qwen3_tts import FasterQwen3TTS
import soundfile
import os

model = FasterQwen3TTS.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base")
voice_design = FasterQwen3TTS.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign")


def create_voice_clone_prompt(ref_audio, ref_text, x_vector_only_mode, speaker):
    if not os.path.exists(f"{speaker}.pt"):
        prompt_items = model.model.create_voice_clone_prompt(
            ref_audio=ref_audio,
            ref_text=ref_text,
            x_vector_only_mode=x_vector_only_mode,
        )
        spk_emb = prompt_items[0].ref_spk_embedding
        torch.save(spk_emb.detach().cpu(), f"{speaker}.pt")
    spk_emb = torch.load(f"{speaker}.pt", weights_only=True).to(model.device)
    voice_clone_prompt = {
        "ref_spk_embedding": [spk_emb],
    }
    return voice_clone_prompt


def generate(
    filename: str,
    text: str,
    voice_clone_prompt,
    instruct=None,
    temperature: float = 0.9,
    top_k: int = 50,
    top_p: float = 1.0,
    repetition_penalty: float = 1.05,
    xvec_only: bool = False,
):
    audio_list, sr = model.generate_voice_clone(
        text=text,
        language="English",
        voice_clone_prompt=voice_clone_prompt,
        instruct=instruct,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        xvec_only=xvec_only,
    )
    soundfile.write(filename, audio_list[0], sr)


def design(
    filename: str,
    text: str,
    instruct: str,
    temperature: float = 0.9,
    top_k: int = 50,
    top_p: float = 1.0,
    repetition_penalty: float = 1.05,
):
    audio_list, sr = voice_design.generate_voice_design(
        text=text,
        language="English",
        instruct=instruct,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
    )
    soundfile.write(filename, audio_list[0], sr)


ref_text = "Just worked out that way. Came to Night City, got my first job, then another... And so on, and so forth"
instruct = "Male, mid-20s, light baritone, fast-talking street cadence, slightly breathy delivery, confident sales tone layered over underlying nervous energy, sentences tend to rush with occasional micro-hesitations, pitch lifts slightly at the end of phrases when uncertain, urban Night City accent with fixer slang, voice tightens under pressure but quickly recovers, expressive but controlled, subtle vocal fry on stressed words"
# design(
#     "patch.wav",
#     text=ref_text,
#     instruct=instruct,
#     repetition_penalty=1.0,
#     top_p=0.98,
#     temperature=0.95,
# )

v_f_file = "v_scene_kerry_default_f_1abf5e82a229f004.wav"
v_f_xvec = create_voice_clone_prompt(
    v_f_file,
    ref_text=ref_text,
    x_vector_only_mode=True,
    speaker="v",
)
# v_f = create_voice_clone_prompt(
#     v_f_file,
#     ref_text=ref_text,
#     x_vector_only_mode=False,
# )

patch_file = "patch.wav"
# patch = create_voice_clone_prompt(
#     patch_file,
#     ref_text=ref_text,
#     x_vector_only_mode=False,
# )
patch_xvec = create_voice_clone_prompt(
    patch_file, ref_text=ref_text, x_vector_only_mode=True, speaker="patch"
)

speaker_to_embed = {"v": v_f_xvec, "patch": patch_xvec}

spoken_lines = {
    "gq000_01_patch_intro_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "You made it. Good. Keep your voice down.",
    },
    "gq000_01_v_choice_ghostline_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Ghostline. Heard the name float around. Never saw the ghosts.",
    },
    "gq000_01_patch_rsp_ghostline_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "That's the point. We're not a gang, not a brand. We listen, collect, move things nobody wants traced.",
    },
    "gq000_01_v_choice_whyyou_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Plenty of mercs in Night City. Why pull me in?",
    },
    "gq000_01_patch_rsp_whyyou_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Because you get in, get out, and don't start asking the wrong questions before the eddies clear.",
    },
    "gq000_01_v_choice_job_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Alright. Talk. What am I doing?",
    },
    "gq000_01_patch_rsp_job_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Tyger Claws are sitting on a relay that looks dead from the street. It isn't. Someone's laundering data through it.",
    },
    "gq000_01_patch_rsp_job_02": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "You jack the node, pull the cache, and drop it where we tell you. Clean job, if nobody gets curious.",
    },
    "gq000_01_v_choice_client_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Tyger Claws don't move like that for free. Who's behind it?",
    },
    "gq000_01_patch_rsp_client_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Someone Arasaka-adjacent. That's all you need. You want names, ask after the job's done.",
    },
    "gq000_01_v_choice_accept_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Fine. Send me the coordinates. I'll get your data.",
    },
    "gq000_01_patch_rsp_accept_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Knew you would. Location's already queued.",
    },
    "gq000_01_patch_rsp_accept_02": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Pull the cache, use the drop point, and don't improvise unless you have to.",
    },
}

for filename, data in spoken_lines.items():
    for i in range(3):
        generate(
            f"{filename}-version{str(i).zfill(2)}.wav",
            data["text"],
            speaker_to_embed[data["speaker"].lower()],
            instruct=None,
            repetition_penalty=1.0,
            temperature=0.95,
            top_p=0.98,
            xvec_only=True,
        )
