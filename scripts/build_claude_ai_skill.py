#!/usr/bin/env python3
"""Create an upload-ready Claude.ai Custom Skill ZIP with standard-library Python.

Only contents of plugins/noslop/skills/noslop are packaged. This does not
upload, publish or install the skill. It validates the resulting archive.
"""
import argparse
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "plugins" / "noslop" / "skills" / "noslop"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MANDATORY = {"SKILL.md", "references/design-rules.md", "references/quality-checks.md"}


def skill_metadata(text):
    front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not front:
        raise ValueError("SKILL.md has no YAML frontmatter")
    block = front.group(1)
    names = re.findall(r"(?m)^name:\s*(.+?)\s*$", block)
    if len(names) != 1:
        raise ValueError("SKILL.md must specify a single name")
    name = names[0].strip("'\"")
    # Supports the documented folded multiline description.
    match = re.search(r"(?m)^description:\s*(>[-+]?|.+)\s*$", block)
    if not match:
        raise ValueError("SKILL.md missing description")
    raw = match.group(1).strip()
    if raw.startswith(">"):
        lines = block[match.end():].lstrip("\n").splitlines()
        text_lines = []
        for line in lines:
            if not line.startswith("  "):
                break
            text_lines.append(line.strip())
        description = " ".join(text_lines)
    else:
        description = raw.strip("'\"")
    return name, description


def validate_source(source=SOURCE):
    root = source.resolve()
    entry = root / "SKILL.md"
    if not entry.is_file():
        raise ValueError("SKILL.md missing")
    name, description = skill_metadata(entry.read_text(encoding="utf-8"))
    if name != root.name or not NAME_PATTERN.fullmatch(name) or len(name) > 64:
        raise ValueError("Invalid skill name or skill folder name mismatch")
    if not description or len(description) > 200:
        raise ValueError("Claude.ai Custom Skills description must be 1–200 characters")
    if "<" in description or ">" in description:
        raise ValueError("XML-style content not allowed in description")
    docs = sorted(p for p in root.rglob("*.md") if p.is_file())
    relative = {p.relative_to(root).as_posix() for p in docs}
    if not MANDATORY.issubset(relative):
        raise ValueError("Missing essential Markdown references")
    for p in docs:
        text = p.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            dest = (p.parent / target).resolve()
            if not dest.is_relative_to(root) or not dest.is_file():
                raise ValueError("Broken/unsafe link: %s -> %s" % (p, target))
    return name, description, docs


def package(output, source=SOURCE):
    name, description, docs = validate_source(source)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in docs:
            arcname = name + "/" + path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=(2024, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity test failed")
        actual = set(archive.namelist())
        expected = {name + "/" + p.relative_to(source).as_posix() for p in docs}
        if actual != expected:
            raise ValueError("ZIP contents differ from expected skill contents")
        if archive.read(name + "/SKILL.md") != (Path(source) / "SKILL.md").read_bytes():
            raise ValueError("SKILL.md differs from source")
    return {"path": str(output), "skill": name, "description_chars": len(description),
            "files": len(docs), "size_bytes": output.stat().st_size}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=REPO_ROOT / "dist" / "noslop-claude-ai.zip")
    args = parser.parse_args()
    print(package(args.output))


if __name__ == "__main__":
    main()
