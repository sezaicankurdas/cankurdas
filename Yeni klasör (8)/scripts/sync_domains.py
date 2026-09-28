#!/usr/bin/env python3
"""Apply approved domain changes to four providers and increment plugin versions."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULES = {
    "DiziPalOriginal": "DiziPalOriginal",
    "HDFilmCehennemi": "HDFilmCehennemi",
    "DiziYou": "DiziYou",
    "FilmMakinesi": "FilmMakinesi",
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Show unapplied changes without writing")
    args = parser.parse_args()
    domains = json.loads((ROOT / "domains.json").read_text(encoding="utf-8"))
    pending = []
    for module, classname in MODULES.items():
        url = domains[module].rstrip("/")
        if not re.fullmatch(r"https://[A-Za-z0-9.-]+", url):
            raise SystemExit(f"Invalid HTTPS domain for {module}: {url}")
        path = ROOT / module / "src/main/kotlin/com/keyiflerolsun" / f"{classname}.kt"
        source = path.read_text(encoding="utf-8")
        match = re.search(r'(override var mainUrl\s*=\s*")([^"]+)(")', source)
        if not match:
            raise SystemExit(f"mainUrl not found in {path}")
        if match.group(2) == url:
            continue
        pending.append((module, match.group(2), url))
        if args.check:
            continue
        source = source[:match.start(2)] + url + source[match.end(2):]
        path.write_text(source, encoding="utf-8")
        build = ROOT / module / "build.gradle.kts"
        gradle = build.read_text(encoding="utf-8")
        version = re.search(r"(?m)^version\s*=\s*(\d+)\s*$", gradle)
        if not version:
            raise SystemExit(f"Version not found in {build}")
        gradle = gradle[:version.start(1)] + str(int(version.group(1)) + 1) + gradle[version.end(1):]
        build.write_text(gradle, encoding="utf-8")
    for module, old, new in pending:
        print(f"{module}: {old} -> {new}")
    if not pending:
        print("Four active providers already match domains.json")
    if args.check and pending:
        raise SystemExit(1)
    print("HDFilmIzle is a tracked URL only; no provider has been verified or built.")


if __name__ == "__main__":
    main()
