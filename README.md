# Qwen3.8-27B at 220 Tokens/s with NInfer

Companion files for the video **[Qwen 3.8 27B at 220 Tokens/Sec Locally — NInfer Tested](https://www.youtube.com/watch?v=xrrcGcsblq0)**.

[![Watch the benchmark](https://img.youtube.com/vi/xrrcGcsblq0/maxresdefault.jpg)](https://www.youtube.com/watch?v=xrrcGcsblq0)

This repository contains the test configuration, prompts, commands, measured results, and verification helpers used in the video. The video contains the explanation, live terminal evidence, application demos, and interpretation.

## What was tested

| Test | Output / context | Decode speed | MTP acceptance | Outcome |
|---|---:|---:|---:|---|
| Standard decoding | 2,048 output tokens | 76.3 tok/s | Off | Completed |
| MTP short run | 2,048 output tokens | 217.6 tok/s | 82.5% | Completed |
| MTP sustained run | 8,192 output tokens | 220.4 tok/s | 85.1% | Hit output limit |
| Compact dashboard | 3,917 output tokens | 206.8 tok/s | 77.2% | Natural stop; UI telemetry did not update in the recording |
| Cluster simulator | 10,114 output tokens | 208.1 tok/s | 78.7% | Natural stop; application worked |
| Long-context code test | 70,268 prompt + 8,000 output tokens | 171.0 tok/s | 69.0% | Prompt processed; output truncated |
| XHigh reasoning | 12,005 output tokens | 182.2 tok/s | 64.8% | Natural stop; complete analysis |

The peak is a measured result for this configuration—not a universal speed claim. Prompt structure, context length, reasoning, sampling, model format, and engine settings materially change performance.

## Test system

- NVIDIA GeForce RTX 5090, 32 GB VRAM
- Qwen3.8-27B NVFP4 NInfer artifact
- NInfer, MTP draft window 3, LM-head draft path
- Greedy decoding for repeatability
- INT8 KV cache
- 64-bit Linux and CUDA 13.1+

See [SETUP.md](SETUP.md), [RUNBOOK.md](RUNBOOK.md), [PROMPTS.md](PROMPTS.md), and [RESULTS.md](RESULTS.md).

## Important compatibility note

NInfer is specialized, not a universal Qwen runtime. It accepts explicitly registered `.ninfer` artifacts and the upstream build currently targets one RTX 5090 (`sm_120a`) on 64-bit Linux. GGUF and ordinary SafeTensors files are not drop-in replacements. Check the upstream requirements before building because supported artifacts and capabilities can change.

## Official project

- [NInfer repository](https://github.com/Neroued/ninfer)
- [NInfer performance methodology](https://github.com/Neroued/ninfer/blob/master/docs/performance.md)
- [Qwen3.8-27B NVFP4 artifact](https://huggingface.co/neroued/Qwen3.8-27B-nvfp4-NInfer)

This is an independent test repository and is not affiliated with the NInfer project.

