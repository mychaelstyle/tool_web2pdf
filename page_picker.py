import os
import sys
import PyPDF2

def pick(pdf_path, page_number, out_path):
    """
    PDFファイルの指定ページをピックして保存します。
    """
    reader = PyPDF2.PdfFileReader(pdf_path)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(reader.getPage(page_number-1))

    with open(out_path, 'wb') as f:
        writer.write(f)

def list_files(dirpath):
    """
    指定フォルダ以下のファイルを再帰的にリストアップし
    (dirpath, filemane)のタプルをyieldで返す

    Parameters
    ----------
    dirname : string
        対象のフォルダパス

    Returns
    -------
    fileinfo : tuple
        (ディレクトリパス, ファイル名)
    """
    for filename in os.listdir(dirpath):
        datetime_string = None
        src_path = os.path.join(dirpath, filename)
        if os.path.isdir(src_path):
            yield from list_files(src_path)
        elif filename.lower().endswith(".pdf"):
            yield ( dirpath, filename )

def main():
    """
    読み込み元フォルダと出力先フォルダのパスを指定して、
    フォルダ内のPDFファイルの1ページ目だけ切り出して出力先に同じフォルダ構成で作成します。
    """
    args = sys.argv

    if 2 >= len(args):
        print("You should use with src folder path and output folder path")
        print("python page_picker.py [src folder path] [output folder path]")
        return

    print("src folder path:%s" % args[1])
    if not os.path.exists(args[1]):
        print("src folder path is not exists!")
        return
    print("Output folder path:%s" % args[2])
    if not os.path.exists(args[2]):
        print("Output folder path is not exists!")
        return

    for (dirpath,filename) in list_files(args[1]):
        pdf_path = os.path.join(dirpath,filename)
        path_diff = dirpath[len(args[1]):]
        out_dir = os.path.join(args[2],path_diff)
        out_path = os.path.join(out_dir,filename)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        print("%s => %s" %(pdf_path,out_path))
        pick(pdf_path, 1, out_path)

if __name__ == '__main__':
    main()

