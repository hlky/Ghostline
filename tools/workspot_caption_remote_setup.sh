#!/usr/bin/env bash
set -euo pipefail
export HF_HOME=/workspace/hf-cache
export UV_LINK_MODE=copy
if ! command -v uv >/dev/null; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
uv venv /workspace/download-venv --python /usr/bin/python3
uv pip install --python /workspace/download-venv/bin/python huggingface_hub
/workspace/download-venv/bin/python -u - <<'PY' > /workspace/model-download.log 2>&1 &
from huggingface_hub import snapshot_download
print(snapshot_download('Qwen/Qwen3.8-27B', revision='1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0'), flush=True)
PY
download_pid=$!
uv venv /workspace/vllm-venv --python /usr/bin/python3
uv pip install --python /workspace/vllm-venv/bin/python vllm==0.32.0 --torch-backend=auto
export PATH=/workspace/vllm-venv/bin:/usr/local/cuda/bin:$PATH
vllm download-kernels
wait "$download_pid"
uv pip freeze --python /workspace/vllm-venv/bin/python > /workspace/vllm-requirements.lock.txt
touch /workspace/CAPTION_ENV_READY
