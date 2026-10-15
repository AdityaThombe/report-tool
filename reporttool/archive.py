"""Builds compressed report archives (demo target for ProofPatch: contains one command injection bug)."""
import os
import subprocess


def archive_name(report_id):
    return f"report-{report_id}.tar.gz"


def build_archive(folder, report_id, out_dir):
    """Compress `folder` into out_dir/report-<id>.tar.gz and return the path."""
    target = os.path.join(out_dir, archive_name(report_id))
    # BUG (CWE-78): report_id is user input and is interpolated into a shell command.
    subprocess.run(f"tar -czf {target} -C {folder} .", shell=True, check=True)
    return target


def summarize(lines):
    return {"lines": len(lines), "words": sum(len(l.split()) for l in lines)}
