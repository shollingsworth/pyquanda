#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test docker images."""
from pathlib import Path
import string
import subprocess
import tempfile
import argparse

BASE = Path(__file__).resolve().parent.parent
DST_DIR = BASE.joinpath("dist")
CACHE_DIR = Path("/tmp/.python_docker_cache/pip")
if not CACHE_DIR.exists():
    _err = True
else:
    _err = any(
        [
            not CACHE_DIR.is_dir(),
            CACHE_DIR.owner() != "root",
        ]
    )

if _err:
    raise SystemExit(f"{CACHE_DIR} needs to exist and be owned by root")

PYTHON_IMG_TYPE = "buster"

SCRIPT_TEMPLATE = string.Template(
    r"""
#!/usr/bin/env bash
set -euo pipefail
IFS=$$'\n\t'
apt update
apt install -y less
pip3 install /$dist_file
/usr/local/bin/pyquanda-cmd demo
""".lstrip()
)


def _get_dist_file() -> Path:
    dst_files = list(DST_DIR.iterdir())
    dlen = len(dst_files)
    if dlen != 1:
        raise SystemExit(
            f"only one dist file should be in {DST_DIR}, {dlen} given"
        )
    return dst_files[0]


def main(args):
    """Run main function."""
    dist_file = _get_dist_file().absolute()
    with tempfile.TemporaryDirectory() as _tdir:
        tdir = Path(_tdir)
        script = tdir.joinpath("run.sh").absolute()
        script.write_text(
            SCRIPT_TEMPLATE.substitute(**{"dist_file": dist_file.name})
        )
        script.chmod(0o0775)
        ver = args.python_version
        docker_img = f"python:{ver}-{PYTHON_IMG_TYPE}"
        name = f"pyquanda-{ver}-{PYTHON_IMG_TYPE}"
        dcmd = [
            "docker",
            "run",
            "--rm",
            "-it",
            "-v",
            f"{CACHE_DIR}:/root/.cache/pip",
            "-v",
            f"{dist_file}:/{dist_file.name}",
            "-v",
            f"{script}:/{script.name}",
            "--name",
            name,
            "--hostname",
            name,
            docker_img,
            "/run.sh",
        ]
        cmd_line = " ".join(dcmd)
        print(f"Running: {cmd_line}")
        rc = subprocess.check_call(
            dcmd,
        )
        if rc != 0:
            raise SystemExit(f"{cmd_line} failed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument(
        "python_version",
        help="python_version help",
        type=str,
    )
    args = parser.parse_args()
    main(args)
