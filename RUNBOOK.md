# Benchmark runbook

Run these from the NInfer source directory after defining `MODEL` and `RESULTS` as shown in [SETUP.md](SETUP.md). Answer content goes to stdout; statistics and diagnostics go to stderr.

## 1. Standard decoding baseline

```bash
./build/apps/ninfer "$MODEL" \
  --prompt "Write a detailed single-file HTML application with embedded CSS and vanilla JavaScript." \
  --max-context 32768 --kv-capacity auto --max-new 2048 \
  --kv-dtype int8 --no-thinking --greedy --log-level info \
  > "$RESULTS/baseline-output.html" 2> "$RESULTS/baseline.log"
```

## 2. MTP short run

Use the same prompt and settings, adding MTP:

```bash
./build/apps/ninfer "$MODEL" \
  --prompt "Write a detailed single-file HTML application with embedded CSS and vanilla JavaScript." \
  --max-context 32768 --kv-capacity auto --max-new 2048 \
  --kv-dtype int8 --spec mtp --draft-tokens 3 --lm-head-draft \
  --no-thinking --greedy --log-level info \
  > "$RESULTS/mtp-short-output.html" 2> "$RESULTS/mtp-short.log"
```

## 3. Sustained 8K output

```bash
./build/apps/ninfer "$MODEL" \
  --prompt "Write a detailed, polished single-file HTML application with embedded CSS and vanilla JavaScript. Return only complete HTML." \
  --max-context 32768 --kv-capacity auto --max-new 8192 \
  --kv-dtype int8 --spec mtp --draft-tokens 3 --lm-head-draft \
  --no-thinking --greedy --log-level info \
  > "$RESULTS/sustained-output.html" 2> "$RESULTS/sustained.log"
```

## 4. Compact dashboard

```bash
PROMPT=$(sed -n '/^## Compact AI GPU dashboard/,/^## /p' PROMPTS.md | sed -n '/^```text$/,/^```$/p' | sed '1d;$d')
./build/apps/ninfer "$MODEL" \
  --prompt "$PROMPT" \
  --max-context 32768 --kv-capacity auto --max-new 4096 \
  --kv-dtype int8 --spec mtp --draft-tokens 3 --lm-head-draft \
  --no-thinking --greedy --log-level info \
  > "$RESULTS/dashboard.html" 2> "$RESULTS/app_run.log"
```

## 5. Cluster simulator

```bash
PROMPT=$(sed -n '/^## AI inference cluster simulator/,/^## /p' PROMPTS.md | sed -n '/^```text$/,/^```$/p' | sed '1d;$d')
./build/apps/ninfer "$MODEL" \
  --prompt "$PROMPT" \
  --max-context 32768 --kv-capacity auto --max-new 12288 \
  --kv-dtype int8 --spec mtp --draft-tokens 3 --lm-head-draft \
  --no-thinking --greedy --log-level info \
  > "$RESULTS/cluster_simulator.html" 2> "$RESULTS/cluster_run.log"
```

## 6. Long-context server

```bash
./build/apps/ninfer-serve "$MODEL" \
  --host 0.0.0.0 --port 9000 \
  --model-id qwen3.8-27b-nvfp4 \
  --max-context 131072 --kv-capacity 131072 --max-concurrency 1 \
  --kv-dtype int8 --spec mtp --draft-tokens 3 --lm-head-draft \
  --no-thinking --greedy --cors --log-stats-interval-ms 1000 \
  --request-log-jsonl "$RESULTS/server_requests.jsonl"
```

In a second terminal:

```bash
python3 tools/build_codebase_request.py "$NINFER_ROOT" "$RESULTS/codebase_request.json"
time curl -sS http://127.0.0.1:9000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  --data-binary @"$RESULTS/codebase_request.json" \
  -o "$RESULTS/codebase_response.json"
```

## 7. XHigh reasoning server and three output budgets

Restart the server without `--no-thinking`:

```bash
./build/apps/ninfer-serve "$MODEL" \
  --host 0.0.0.0 --port 9000 \
  --model-id qwen3.8-27b-nvfp4 \
  --max-context 131072 --kv-capacity 131072 --max-concurrency 1 \
  --kv-dtype int8 --spec mtp --draft-tokens 3 --lm-head-draft \
  --greedy --cors --default-thinking-budget 4096 \
  --log-stats-interval-ms 1000 \
  --request-log-jsonl "$RESULTS/xhigh_requests.jsonl"
```

Create and send each request:

```bash
python3 tools/build_xhigh_request.py 4096 "$RESULTS/xhigh_request_4k.json"
python3 tools/build_xhigh_request.py 8192 "$RESULTS/xhigh_request_8k.json"
python3 tools/build_xhigh_request.py 12288 "$RESULTS/xhigh_request_12k.json"

for size in 4k 8k 12k; do
  time curl -sS http://127.0.0.1:9000/v1/chat/completions \
    -H 'Content-Type: application/json' \
    --data-binary @"$RESULTS/xhigh_request_${size}.json" \
    -o "$RESULTS/xhigh_response_${size}.json"
done
```

Inspect a response from PowerShell:

```powershell
.\tools\inspect_response.ps1 .\ninfer-results\xhigh_response_12k.json
```

The short baseline prompt above is normalized for reproducibility; generated content affects acceptance and exact speed. The published figures are the measurements from the recorded runs, not guaranteed targets.

