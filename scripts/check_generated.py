#!/usr/bin/env python3
"""Check that generated files match their sources.

Run after scripts/build_diagrams.py and scripts/build_office.py. Any file those
scripts changed must differ from the committed copy only in zip packaging (for
.docx/.xlsx, where compression can vary between zlib versions); otherwise the
committed file is stale and the build scripts need to be re-run.
"""
import io
import subprocess
import sys
import zipfile

GENERATED = ("docs/diagrams/", "forms/word/", "inventory/AI-Inventory.xlsx")
EXTENSIONS = (".svg", ".drawio", ".docx", ".xlsx")


def members(data):
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        return {n: z.read(n) for n in z.namelist()}


def main():
    changed = subprocess.run(["git", "status", "--porcelain", "--", *GENERATED],
                             capture_output=True, text=True, check=True).stdout.splitlines()
    stale = []
    for line in changed:
        status, path = line[:2], line[3:]
        if not path.endswith(EXTENSIONS):
            continue
        if status.strip() != "M" or not path.endswith((".docx", ".xlsx")):
            stale.append(path)
            continue
        old = subprocess.run(["git", "show", f"HEAD:{path}"], capture_output=True, check=True).stdout
        with open(path, "rb") as fh:
            new = fh.read()
        if members(old) != members(new):
            stale.append(path)
    for p in stale:
        print(f"stale: {p}")
    if stale:
        print("Generated files are out of date. Run: python3 scripts/build_diagrams.py && "
              "python3 scripts/build_office.py, then commit the results.")
        return 1
    print("generated files are current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
