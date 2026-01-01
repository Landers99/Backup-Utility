from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


@dataclass(frozen=True)
class VerifyRequest:
    src: Path
    dest: Path
    excludes: Sequence[str]


def verify_cmd(args) -> None:
    req = VerifyRequest(
        src=args.src,
        dest=args.dest,
        excludes=args.exclude)
    ok = run_verify(req)
    raise SystemExit(0 if ok else 2)


def run_verify(req: VerifyRequest) -> bool:
    # TODO:
    # - compare src/dest trees
    # - report missing/mismatched
    raise NotImplementedError("verify is not implemented yet")
