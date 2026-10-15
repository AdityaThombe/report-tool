import os
import pytest
from reporttool.archive import build_archive

def test_report_id_command_injection(tmp_path):
    # prepare a dummy folder with a file
    src = tmp_path / "src"
    src.mkdir()
    (src / "dummy.txt").write_text("data")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    # malicious report_id that injects a touch command
    malicious_id = f"x; touch {tmp_path / 'pwned'} #"
    try:
        build_archive(str(src), malicious_id, str(out_dir))
    except Exception:
        # the safe implementation may raise due to invalid archive name
        pass
    # the injected file must not exist
    assert not (tmp_path / "pwned").exists()
