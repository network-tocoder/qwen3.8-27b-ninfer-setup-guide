import json
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
destination = Path(sys.argv[2]).resolve()
patterns = ("include/**/*.h", "include/**/*.hpp", "src/**/*.h", "src/**/*.hpp", "src/**/*.cc", "src/**/*.cpp", "src/**/*.cu", "apps/**/*.cc", "apps/**/*.cpp")
files = sorted({path for pattern in patterns for path in root.glob(pattern) if path.is_file()})
sections = []
for path in files:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    sections.append(f"\n===== {path.relative_to(root)} =====\n{text}")
source = "".join(sections)
task = "Study the supplied NInfer C++, CUDA, headers, and implementation files. Generate a polished interactive, self-contained HTML NInfer architecture explorer. Use only components that can be supported by the supplied source. Include the styling and JavaScript in the same file. No external libraries and no markdown fences. Return only valid HTML ending with </html>."
content = f"{task}\n\nSOURCE:\n{source}"
payload = {
    "model": "qwen3.8-27b-nvfp4",
    "messages": [{"role": "user", "content": content}],
    "max_tokens": 8000,
    "temperature": 0,
}
destination.write_text(json.dumps(payload), encoding="utf-8")
print(f"Files: {len(files)}")
print(f"Source context characters: {len(source)}")
print(destination)

