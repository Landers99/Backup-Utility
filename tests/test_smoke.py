from backup_cli.cli import build_parser


def test_cli_builds():
    parser = build_parser()
    assert parser is not None
