# Recorded results

| Workload | Prompt tokens | Output tokens | Finish | Time | Prefill | Decode | Overall | MTP acceptance |
|---|---:|---:|---|---:|---:|---:|---:|---:|
| Baseline, MTP off | Short | 2,048 | Length | 26.9 s | — | 76.3 | 76.2 | — |
| MTP short | Short | 2,048 | Length | 9.4 s | — | 217.6 | — | 82.5% |
| MTP sustained | Short | 8,192 | Length | 37.2 s | — | 220.4 | 220.2 | 85.1% |
| Compact dashboard | 74 | 3,917 | Stop token | 19.0 s | 1.60K | 206.8 | 206.4 | 77.2% |
| Cluster simulator | Short | 10,114 | Stop token | 48.6 s | — | 208.1 | 207.9 | 78.7% |
| Long-context source | 70,268 | 8,000 | Length | 59.8 s | 5.43K | 171.0 | — | 69.0% |
| XHigh final | 195 | 12,005 total | Stop token | ~66 s | — | 182.2 | — | 64.8% |

Speeds are tokens per second. The long-context TTFT was 13.0 seconds. The final XHigh response reported 4,120 reasoning tokens.

## Completion versus correctness

- The 8,192-token sustained run was fast but stopped mid-application.
- The compact dashboard closed correctly, but its recorded telemetry stayed at zero and its chart remained empty.
- The cluster simulator completed naturally and its controls, queue, charts, failure injection, and recovery worked.
- Cluster telemetry was intentionally simulated; only the NInfer terminal statistics were measured hardware telemetry.
- The long-context request was processed successfully, but its 8,000-token HTML response was truncated.
- The 4K XHigh run spent its allowance on reasoning and produced no visible final answer. The 8K run produced visible content but still finished for length. The 12K run stopped naturally.

These are single recorded runs, not multi-seed benchmark averages. Compare them with the upstream project's controlled methodology before drawing broader conclusions.

