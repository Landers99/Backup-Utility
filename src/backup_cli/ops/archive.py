from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class ArchiveRequest:
    src: Path
    out_dir = Path
    fmt: str  # "zip" | "tar.gz"
    excludes: Sequence[str]
    dry_run: bool


def archive_cmd(args) -> None:
    req = ArchiveRequest(
        src=args.src,
        out_dir=args.out_dir,
        fmt=args.format,
        excludes=args.exclude,
        dry_run=args.dry_run,
    )
    run_archive(req)


def run_archive(req: ArchiveRequest) -> None:
    # TODO:
    # - validate paths
    # - build archive name
    # - stream files into archive (zip or tar.gz)
    raise NotImplementedError("archive is not implemented yet")
