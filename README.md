# Backup-Utility

A CLI tool that copies files/directories to a backup destination and optionally creates an archive—reliably, repeatably, and with clear output.

## Purpose

This project explores reliable file backup and archiving workflows by building a boring, script-friendly CLI system utility that copies, verifies, and optionally archives directories with predictable behavior and clear output. The goal is correctness and clarity, not scale.

## Scope

### What does it do?

Core behaviors:

* Backup (mirror or incremental copy)
  * Copy a source path -> destination path
  * "Mirror" mode (destination becomes an exact copy: add/update/delete to match)
  * "Incremental" mode (only add/update; no deletes)
* Archive
  * Create a timestamped archive file (e.g. `.tar.zst` or `.zip`) from a source path
  * Store it at a destination directory (local disk, external drive, mounted network path)
* Excludes
  * Include/exclude patterns (globs), like `--exclude node_modules --exclude "*.tmp"`
* Safety + Usability
  * Dry-run mode (show what would happen)
  * Checksums optional (verify copied files)
  * Logs (human-readable + JSON)
  * Exit codes that make scripting sane

Minimal commands:

* `backup copy <src> <dest> [--incremental|--mirror] [--exclude ...] [--dry-run] [--verify]`
* `backup archive <src> <dest-dir> [--format tar.zst|zip] [--exclude ...]`
* `backup verify <src> <dest>`

### What does it NOT do?
* No cloud provider integration
* No encrpytion/key management
* No GUI
* No deduplication or block-level incremental backups
* No snapshotting/filesystem-native features
* No background daemon/scheduler
* No database/backup catalog

## Constraints
* Must be restartable and safe - backups may get interrupted (laptop sleeps, drive unplugged, power loss)
  * Write temp files then atomic rename
  * Use a journal/manifest so reruns continue cleanly
  * Never leave destination in a corrupted half-state

## Tech Stack
* Python: fast iteration, acceptable performance for personal use
* UV: manage project dependencies and environment

## Install
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
