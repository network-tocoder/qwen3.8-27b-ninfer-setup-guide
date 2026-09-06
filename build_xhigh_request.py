import json
import sys
from pathlib import Path

budget = int(sys.argv[1])
destination = Path(sys.argv[2])
prompt = '''Review this asynchronous money-transfer function:

async def transfer(src, dst, amount):
    async with locks[src]:
        if balances[src] < amount:
            raise ValueError("insufficient")
        await asyncio.sleep(0)
        async with locks[dst]:
            balances[src] -= amount
            balances[dst] += amount

Concurrent transfers may run in either direction, tasks may be cancelled, and accounts may be created dynamically. Identify every concurrency and correctness failure, demonstrate a concrete failing interleaving, provide production-safe corrected Python, define its invariants, and write deterministic tests for deadlock, cancellation, negative amounts, and conservation of total balance.'''
payload = {
    "model": "qwen3.8-27b-nvfp4",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": budget,
    "reasoning_effort": "xhigh",
    "temperature": 0,
}
destination.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(destination)

