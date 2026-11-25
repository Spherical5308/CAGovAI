#!/usr/bin/env python3
"""Check that relative links and #anchors in the repository's Markdown files resolve.

External (http/https/mailto) links are not fetched. Exit code 1 if any link is broken.
Usage: python3 scripts/check_links.py [repo_root]
"""
import os
import re
import sys

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
SKIP_DIRS = {".git", "node_modules"}


def slug(text):
    """Approximate GitHub's heading anchor."""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path, cache={}):
    if path not in cache:
        found, counts, in_code = set(), {}, False
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.lstrip().startswith("```"):
                    in_code = not in_code
                    continue
                m = None if in_code else HEADING.match(line)
                if m:
                    base = slug(m.group(2))
                    n = counts.get(base, 0)
                    found.add(base if n == 0 else f"{base}-{n}")
                    counts[base] = n + 1
        cache[path] = found
    return cache[path]


def main(root):
    broken = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            src = os.path.join(dirpath, name)
            in_code = False
            with open(src, encoding="utf-8") as fh:
                for lineno, line in enumerate(fh, 1):
                    if line.lstrip().startswith("```"):
                        in_code = not in_code
                    if in_code:
                        continue
                    for target in LINK.findall(line):
                        if re.match(r"^[a-z]+:", target):
                            continue
                        path, _, frag = target.partition("#")
                        dest = os.path.normpath(os.path.join(dirpath, path)) if path else src
                        if not os.path.exists(dest):
                            broken.append(f"{src}:{lineno}: missing file {target}")
                        elif frag and dest.endswith(".md") and frag.lower() not in anchors(dest):
                            broken.append(f"{src}:{lineno}: missing anchor {target}")
    for b in broken:
        print(b)
    print(f"{len(broken)} broken link(s)")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
