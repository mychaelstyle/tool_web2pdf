import subprocess, time, os, sys
import pandas as pd

chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def get_pdf(url, save_file_path):
    proc = subprocess.run([chrome,"--headless"," --disable-gpu","--print-to-pdf=%s"%save_file_path,"-crash-dumps-dir=%s"%save_file_path, url])
#            stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    if not proc.stdout is None:
        print(proc.stdout.decode("utf8"))

    if not proc.stderr is None:
        print(proc.stderr.decode("utf8"))

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

    df = pd.read_excel(args[1],sheet_name=args[2])
    for index, row in df.iterrows():
        print("%s:%s:%s" % (row[0],row[1],row[2]))
        outpath = os.path.join(args[3], '%s.pdf' % row[0])
        get_pdf(row[2], outpath)
    
if __name__ == '__main__':
    main()

