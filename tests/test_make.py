import os
import pytest
import make
import shutil
import time

def test_to_pdf():
    tmpdir = "fixtures/tmp"
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)
    make.to_pdf("https://google.com/", tmpdir, "google.pdf")
    outpath = os.path.join(tmpdir,"google.pdf")
    assert os.path.exists(outpath)
    assert os.path.getsize(outpath)>0
    os.remove(outpath)
    shutil.rmtree(tmpdir)

def test_read_excel_rows():
    for (i,url,cat) in make.read_excel_rows("fixtures/data.xlsx","Sheet1"):
        print("%s:%s:%s" % (i,url,cat))
        assert not i is None
        assert not url is None
        assert not cat is None
        assert i in [3333,4444,5555] 
        assert cat in ["Google","Yahoo","Goo"] 
        assert url in [
                "https://www.google.com/",
                "https://www.yahoo.co.jp/",
                "https://www.goo.ne.jp/"]

    for (i,url,cat) in make.read_excel_rows("fixtures/data.xlsx","Sheet2"):
        print("%s:%s:%s" % (i,url,cat))
        assert not i is None
        assert not url is None
        assert cat is None

