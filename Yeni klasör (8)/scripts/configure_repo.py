#!/usr/bin/env python3
"""Set the public GitHub repository path in build metadata and repo.json."""
import json
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", sys.argv[1]):
    raise SystemExit("Usage: python scripts/configure_repo.py GITHUB_USER/REPOSITORY")
root = Path(__file__).resolve().parents[1]
slug = sys.argv[1]
build = root / "build.gradle.kts"
source = build.read_text(encoding="utf-8")
source = re.sub(r'https://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+(?=")', f'https://github.com/{slug}', source, count=1)
build.write_text(source, encoding="utf-8")
manifest = {
    "name": "Kisisel CloudStream Deposu",
    "description": "Dort secili kaynak; besinci kaynak gelistirme asamasinda",
    "manifestVersion": 1,
    "pluginLists": [f"https://raw.githubusercontent.com/{slug}/builds/plugins.json"],
}
(root / "repo.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"CloudStream URL: https://raw.githubusercontent.com/{slug}/builds/repo.json")
