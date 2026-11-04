#!/usr/bin/env python3
"""Basic offline HTML artifact lint. Not a browser, accessibility or factual audit."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class OutlineParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.lang = ""
        self.viewport = False
        self.ids = []
        self.title = False
        self.title_text = ""
        self._inside_title = False
        self.broken_links = []

    def handle_starttag(self, tag, attrs):
        at = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.lang = at.get("lang") or ""
        if tag == "meta" and at.get("name", "").lower() == "viewport":
            self.viewport = bool(at.get("content"))
        if tag == "title":
            self._inside_title = True
            self.title = True
        if at.get("id"):
            self.ids.append(at["id"])
        if tag == "a" and not at.get("href"):
            self.broken_links.append("Link without href")

    def handle_endtag(self, tag):
        if tag == "title":
            self._inside_title = False

    def handle_data(self, data):
        if self._inside_title:
            self.title_text += data


def validate_html(text):
    parser = OutlineParser()
    parser.feed(text)
    errors = []
    if "html" not in parser.tags:
        errors.append("Missing html element")
    if not parser.lang:
        errors.append("Missing html lang attribute")
    if not parser.title or not parser.title_text.strip():
        errors.append("Missing nonempty title")
    if not parser.viewport:
        errors.append("Missing viewport meta tag")
    if "h1" not in parser.tags:
        errors.append("Missing h1")
    if "main" not in parser.tags:
        errors.append("Missing main landmark")
    if "button" in parser.tags and not re.search(r"(onclick|addEventListener|onClick|<script|type=['\"]submit)", text, re.I):
        errors.append("Buttons present, but no interaction code detected (heuristic)")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("Duplicate DOM IDs")
    errors.extend(parser.broken_links)
    return errors


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("file", type=Path, help="HTML file to lint")
    opts = arg.parse_args()
    if not opts.file.exists():
        arg.error("File not found")
    errors = validate_html(opts.file.read_text(encoding="utf-8"))
    print(json.dumps({"file": str(opts.file), "errors": errors,
                      "scope": "static HTML checks only; does not assess first-screen words, factual fidelity or browser behavior"},
                     ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
