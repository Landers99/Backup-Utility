from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class CopyRequest:
    src: Path
    dest: Path
    mode: str  # "incremental" | "mirror"
    excludes: Sequence[str]
    dry_run: bool

def copy_cmd(args) -> None:
    req = CopyRequest(
        src=args.src,
        dest=args.dest,
        mode=args.mode,
        excludes=args.exclude,
        dry_run=args.dry_run,
    )
    run_copy(req)


def run_copy(req: CopyRequest) -> None:
    # TODO:
    # - validate paths
    # - walk filesystem
    # - apply excludes
    # - copy files (atomic)
    # - if mirror: delete extras
    raise NotImplementedError("copy is not implemented yet")
