#!/usr/bin/env python3
"""Fetch every external http(s) link in the repository's Markdown files and report broken ones.

A link is broken when it cannot be reached, returns HTTP 404/410 or another error status,
or lands on a page whose title says it was not found. A link that redirects to a different
page is listed as a warning, because State sites move pages that way.

Run monthly by .github/workflows/external-links.yml, which opens an issue when links break.
Exit code 1 if any link is broken. Uses only the standard library.
Usage: python3 scripts/check_external_links.py [repo_root] [--report report.md]
"""
import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit

URL = re.compile(r"https?://[^\s)<>\"'`\]]+")
SKIP_DIRS = {".git", "node_modules"}
# Hosts that refuse scripted requests; a 401/403/429 from them is not treated as broken.
BOT_BLOCKING = {"github.com", "www.linkedin.com"}
NOT_FOUND_TITLE = re.compile(r"<title>[^<]*(not found|404|page cannot be found|no longer available)", re.I)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8",
}


def find_urls(root):
    """Map each URL to the files that contain it."""
    urls = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as fh:
                for url in URL.findall(fh.read()):
                    url = url.rstrip(".,;:")
                    urls.setdefault(url, set()).add(os.path.relpath(path, root))
    return urls


def fetch(url, timeout=30):
    """Return (status, final_url, note). status is an int, or None when unreachable."""
    note = ""
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                head = resp.read(65536).decode("utf-8", "replace")
                if "html" in resp.headers.get("Content-Type", "") and NOT_FOUND_TITLE.search(head):
                    return 404, resp.geturl(), "page title says not found"
                return resp.status, resp.geturl(), ""
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503, 504) and attempt == 0:
                time.sleep(5)
                continue
            return exc.code, url, exc.reason if isinstance(exc.reason, str) else ""
        except Exception as exc:  # DNS, TLS, timeout, connection reset
            note = f"{type(exc).__name__}: {exc}"
            if attempt == 0:
                time.sleep(5)
    return None, url, note


def same_page(a, b):
    """True when a redirect only changed scheme, a www. prefix or a trailing slash."""
    def norm(u):
        p = urlsplit(u)
        return (p.netloc.lower().removeprefix("www."), p.path.rstrip("/"), p.query)
    return norm(a) == norm(b)


def check(urls):
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = dict(zip(urls, pool.map(fetch, urls)))
    broken, moved = [], []
    for url, (status, final, note) in sorted(results.items()):
        host = urlsplit(url).netloc.lower()
        if status is not None and 200 <= status < 400:
            if not same_page(url, final):
                moved.append((url, final))
        elif host in BOT_BLOCKING and status in (401, 403, 429):
            continue
        else:
            broken.append((url, status, note))
    return broken, moved


def report(urls, broken, moved):
    lines = [f"Checked {len(urls)} external links in the repository's Markdown files.", ""]
    if broken:
        lines += ["## Broken", "", "| Link | Result | Found in |", "|---|---|---|"]
        for url, status, note in broken:
            result = f"HTTP {status}" if status else "unreachable"
            if note:
                result += f" ({note})"
            lines.append(f"| {url} | {result} | {', '.join(sorted(urls[url]))} |")
        lines.append("")
    if moved:
        lines += ["## Redirected (check the new page is still the right one)", "",
                  "| Link | Now goes to | Found in |", "|---|---|---|"]
        for url, final in moved:
            lines.append(f"| {url} | {final} | {', '.join(sorted(urls[url]))} |")
        lines.append("")
    if not broken and not moved:
        lines.append("All external links work.")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--report", help="also write the report to this Markdown file")
    args = ap.parse_args()
    urls = find_urls(args.root)
    broken, moved = check(list(urls))
    text = report(urls, broken, moved)
    print(text)
    if args.report:
        with open(args.report, "w", encoding="utf-8") as fh:
            fh.write(text)
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
