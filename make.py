import subprocess, time, os, sys
import pandas as pd

# Google Chromeコマンドのパス
PATH_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# PDFのファイル名となるExcelの列ラベル名
COLUMN_LABEL_ID = "ID"
# PDFにするURLを記述するExcelの列ラベル名
COLUMN_LABEL_URL = "URL"
# PDFを保存する振り分けフォルダ名を記述するExcelの列ラベル名
COLUMN_LABEL_CATEGORY = "Category"

def to_pdf(url, output_folder, file_name):
    tmpdir = os.path.join(output_folder,"tmp")
    if not os.path.exists(output_folder):
        raise FileNotFoundError("%s is not found!" % output_folder)
    elif not os.path.isdir(output_folder):
        raise Exception("%s is not a folder!" % output_folder)
    if not os.path.exists(tmpdir):
        os.mkdir(tmpdir)
    save_file_path = os.path.join(output_folder,file_name)
    proc = subprocess.run(
            [
                PATH_CHROME,
                "--headless",
                " --disable-gpu",
                "--print-to-pdf=%s"%save_file_path,
                "-crash-dumps-dir=%s"%tmpdir,
                url])

    if not proc.stdout is None:
        print(proc.stdout.decode("utf8"))

    if not proc.stderr is None:
        print(proc.stderr.decode("utf8"))

def read_excel_rows(file_path,sheet):
    if not os.path.exists(file_path):
        raise FileNotFoundError("%s is not found!" % file_path)
    df = pd.read_excel(file_path,sheet_name=sheet)
    if not COLUMN_LABEL_ID in df.columns:
        raise KeyError("%s label is not found!"%COLUMN_LABEL_ID)
    if not COLUMN_LABEL_URL in df.columns:
        raise KeyError("%s label is not found!"%COLUMN_LABEL_URL)
    for index, row in df.iterrows():
        if COLUMN_LABEL_CATEGORY in df.columns:
            yield (row[COLUMN_LABEL_ID], row[COLUMN_LABEL_URL], row[COLUMN_LABEL_CATEGORY])
        else:
            yield (row[COLUMN_LABEL_ID], row[COLUMN_LABEL_URL], None)

def main():
    args = sys.argv

    print(args)

    if 3 >= len(args):
        print("You should use with excel file path, sheet name and output folder path")
        print("python make.py [excel file path] [excel sheet name] [output folder path]")
        return

    print("Excel path:%s" % args[1])
    if not os.path.exists(args[1]):
        print("Excel file path is not exists!")
        return
    print("Sheet name:%s" % args[2])
    print("Output folder path:%s" % args[3])
    if not os.path.exists(args[3]):
        print("Output folder path is not exists!")
        return

    for (file_id,url,category) in read_excel_rows(args[1],args[2]):
        print("%s:%s:%s" % (file_id,url,category))
        file_name = "%s.pdf" % file_id
        out_dir = args[3]
        if not category is None:
            out_dir = os.path.join(out_dir, category)
        to_pdf(url, out_dir,file_name)
    
if __name__ == '__main__':
    main()

