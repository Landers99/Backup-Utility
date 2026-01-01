from __future__ import annotations

import argparse
from pathlib import Path

from .logging_utils import setup_logging
from .ops.archive import archive_cmd
from .ops.copy import copy_cmd
from .ops.verify import verify_cmd


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="backup", description="Boring backup/archive CLI (skeleton).")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")

    sub = p.add_subparsers(dest="cmd", required=True)

    p_copy = sub.add_parser("copy", help="Copy src -> dest (stub).")
    p_copy.add_argument("src", type=Path)
    p_copy.add_argument("dest", type=Path)
    p_copy.add_argument("--mode", choices=["incremental", "mirror"], default="incremental")
    p_copy.add_argument("--exclude", action="append", default=[])
    p_copy.add_argument("--dry-run", action="store_true")
    p_copy.set_defaults(func=copy_cmd)

    p_arch = sub.add_parser("archive", help="Create archive from src (stub).")
    p_arch.add_argument("src", type=Path)
    p_arch.add_argument("out_dir", type=Path)
    p_arch.add_argument("--format", choices=["zip", "tar.gz"], default="zip")
    p_arch.add_argument("--exclude", action="append", default=[])
    p_arch.add_argument("--dry-run", action="store_true")
    p_arch.set_defaults(func=archive_cmd)

    p_ver = sub.add_parser("verify", help="Verify src/dest (stub).")
    p_ver.add_argument("src", type=Path)
    p_ver.add_argument("dest", type=Path)
    p_ver.add_argument("--exclude", action="append", default=[])
    p_ver.set_defaults(func=verify_cmd)

    return p


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    setup_logging(args.verbose)
    args.func(args)
