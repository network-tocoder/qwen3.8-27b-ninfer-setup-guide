# Setup

The commands below follow the upstream source-build workflow. Recheck the [official README](https://github.com/Neroued/ninfer) before running them.

## Requirements

- 64-bit Linux
- NVIDIA GeForce RTX 5090 (`sm_120a`)
- CUDA Toolkit 13.1 or newer and a compatible driver
- CMake 3.28+, Ninja, a C++20 compiler, `pkg-config`
- FFmpeg development libraries and `libcurl >= 7.85`
- Python 3 and the Hugging Face CLI for the helper commands in this repository

## Build

```bash
git clone https://github.com/Neroued/ninfer.git
cd ninfer
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build --parallel
```

## Download the tested artifact

```bash
mkdir -p models
hf download neroued/Qwen3.8-27B-nvfp4-NInfer \
  qwen3_8_27b_nvfp4.ninfer \
  --local-dir models
```

The commands in [RUNBOOK.md](RUNBOOK.md) assume:

```bash
export NINFER_ROOT="$PWD"
export MODEL="$NINFER_ROOT/models/qwen3_8_27b_nvfp4.ninfer"
export RESULTS="$NINFER_ROOT/ninfer-results"
mkdir -p "$RESULTS"
```

NInfer has no official packaged installer in the upstream repository; run it from the source build tree.

