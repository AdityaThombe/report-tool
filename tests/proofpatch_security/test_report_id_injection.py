import pytest
from reporttool.archive import build_archive

def test_report_id_injection_has_no_effect(tmp_path):
    folder = tmp_path / "data"
    folder.mkdir()
    (folder / "file.txt").write_text("content")
    out_dir = tmp_path / "out"
    out_dir.mkdir()
    malicious_id = f"1.tar.gz; touch {tmp_path}/hacked #"
    try:
        build_archive(str(folder), malicious_id, str(out_dir))
    except Exception:
        pass
    assert not (tmp_path / "hacked").exists()
