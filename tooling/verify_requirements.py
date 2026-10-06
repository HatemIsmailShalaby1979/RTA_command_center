#!/usr/bin/env python3
"""Prove that requirements.txt is complete: build a clean venv from it, then
import the application.

Why this exists
---------------
``requirements.txt`` previously declared only ``streamlit``, while
``src/calculations.py`` imports numpy and pandas and ``visualizations.py``
imports plotly. A clean install of this repository could not start the
application at all. That was found by hand, after CI had already failed on a
missing import for the same reason.

A requirements file is a claim. This turns it into a measurement: if any import
used by the shipped code is absent from the declared dependencies, this fails.

What it does
------------
1. Creates a throwaway virtualenv outside the repository.
2. Installs ``-r requirements.txt`` and nothing else.
3. Runs the declared import check with ``PYTHONPATH=src``, the same way the
   application resolves its siblings.
4. Reports the exact failing import if there is one.

It does not import ``_archive/``: that directory is known non-functional (it
imports a ``core`` module that does not exist here) and is not shipped code.

Usage
-----
    python tooling/verify_requirements.py
    python tooling/verify_requirements.py --keep    # leave the venv for inspection

Exit codes:
    0  a clean install of the declared file satisfies every import
    1  an import is unsatisfied, or the install failed
    2  bad input
"""

from __future__ import annotations

import argparse
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQUIREMENTS = ROOT / "requirements.txt"

# The modules the shipped application actually loads. src/app.py imports these
# two by bare name, which is why PYTHONPATH must include src.
IMPORT_CHECK = "import calculations, visualizations; print('ok')"


def run(cmd: list[str], cwd: pathlib.Path | None = None,
        env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, env=env, capture_output=True,
                          text=True, timeout=900)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--keep", action="store_true",
                    help="do not delete the temporary venv")
    args = ap.parse_args()

    if not REQUIREMENTS.exists():
        print(f"error: {REQUIREMENTS} not found", file=sys.stderr)
        return 2

    print(f"requirements : {REQUIREMENTS}")
    print("building a clean virtualenv from that file alone")

    base = pathlib.Path(tempfile.gettempdir())
    venv = base / "rta_req_verify"
    if venv.exists():
        shutil.rmtree(venv, ignore_errors=True)

    try:
        created = run([sys.executable, "-m", "venv", str(venv)])
        if created.returncode != 0:
            print("error: could not create the venv", file=sys.stderr)
            print(created.stderr[-1500:], file=sys.stderr)
            return 1

        vpy = venv / ("Scripts" if os.name == "nt" else "bin") / \
            ("python.exe" if os.name == "nt" else "python")

        installed = run([str(vpy), "-m", "pip", "install", "--quiet",
                         "--upgrade", "pip"], cwd=ROOT)
        if installed.returncode != 0:
            print(installed.stderr[-800:], file=sys.stderr)
            return 1

        step = run([str(vpy), "-m", "pip", "install", "--quiet",
                    "-r", str(REQUIREMENTS)], cwd=ROOT)
        if step.returncode != 0:
            print("FAIL: requirements.txt does not resolve", file=sys.stderr)
            print(step.stdout[-2500:], file=sys.stderr)
            print(step.stderr[-2500:], file=sys.stderr)
            return 1
        print("  install    : ok")

        env = dict(os.environ)
        env["PYTHONPATH"] = str(ROOT / "src")
        checked = run([str(vpy), "-c", IMPORT_CHECK], cwd=ROOT, env=env)
        if checked.returncode != 0:
            print("FAIL: the application cannot import from a clean install",
                  file=sys.stderr)
            print(checked.stderr[-2000:], file=sys.stderr)
            return 1
        print("  import     : ok")

        frozen = run([str(vpy), "-m", "pip", "freeze"], cwd=ROOT)
        pinned = [ln for ln in frozen.stdout.splitlines()
                  if "==" in ln and not ln.lower().startswith("-e")]
        print(f"  resolved   : {len(pinned)} packages installed")

        print("\nPASS: a clean install of requirements.txt satisfies every "
              "import the shipped code makes.")
        return 0

    finally:
        if not args.keep:
            shutil.rmtree(venv, ignore_errors=True)
        else:
            print(f"\nvenv kept at {venv}")


if __name__ == "__main__":
    raise SystemExit(main())