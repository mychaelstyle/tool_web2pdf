import os
import pytest
import page_picker
import shutil
import time


def test_pick():
    tmpdir = "fixtures/tmp"
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)
    pdf_path = "fixtures/Yahoo.pdf"
    out_path = os.path.join(tmpdir,"Yahoo.pdf")
    page_picker.pick(pdf_path, 1, out_path)
    assert os.path.exists(out_path)
    assert os.path.getsize(pdf_path) > os.path.getsize(out_path)
    os.remove(out_path)


