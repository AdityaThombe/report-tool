import os
import tarfile

from reporttool.archive import archive_name, build_archive, summarize


def test_archive_name():
    assert archive_name("42") == "report-42.tar.gz"


def test_build_archive_contains_files(tmp_path):
    src = tmp_path / "src"
    src.mkdir()
    (src / "a.txt").write_text("hello")
    out = tmp_path / "out"
    out.mkdir()
    path = build_archive(str(src), "7", str(out))
    assert os.path.exists(path)
    with tarfile.open(path) as tar:
        assert any(m.name.endswith("a.txt") for m in tar.getmembers())


def test_summarize():
    assert summarize(["a b", "c"]) == {"lines": 2, "words": 3}
