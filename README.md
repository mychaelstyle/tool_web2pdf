tool_web2pdf
============

MacOS上でExcelに書かれたWebページURLのリストからChromeのコマンドラインheadlessから実行して指定のフォルダにPDFで保存します。

Webアプリケーションで表示している指定の大量の詳細ページを3000以上を来週までにPDF化して印刷屋に回せるようにnnnnn.pdfのような規則正しい名前でPDF出力できるようにしてくれなどの指示が突然降ってきてお困りのあなたに最適な簡単なスクリプトです。

Environment
===========

- Mac OS X >= 10.3
- python >= 3.7
- anaconda3 >= 2019.03
- PyPDF2
- Google Chrome >= 77.0.3865.90 (Official Build)

How to use
===========

Excelのフォーマット
------------------

- 一行目をラベル名とし、二行目から実行されます。
- ファイル名にしたい列ラベルを ID としてください。
- アクセスしてPDF化したいURLを記述する列ラベルを URL としてください。
- 出力先のフォルダを分けたい場合は、フォルダ名を記述する列ラベルを Category としてください。この名前の列がなければフォルダ分けされず、指定された出力フォルダ内に全て出力されます。

サンプルはtext/fixtures/data.xlsxの内容をみてください。

実行方法
--------
最初に使うときは下記を実行

    python setup.py install

ExcelからURLのPDFを生成するにはターミナルを起動してクローンしたフォルダの中に移動し、下記のコマンドを実行してください。

    python make.py [excel file path] [excel sheet name] [output folder path]

フォルダ内のPDFを全てサーチして1ページ目だけ指定した出力フォルダに出力するには下記のコマンドを実行してください。

    python page_picker.py [Source folder path] [Output folder path]

How to use on another OS
========================

make.pyの4行目,以下の行のChromeコマンドのパスを自分の環境のパスに書き換えて実行してください。

   PATH_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

How to use another excel format
===============================

make.pyの下記の行を変更することでラベル名を変更できます。

COLUMN_LABEL_ID = "ID"
COLUMN_LABEL_URL = "URL"
COLUMN_LABEL_CATEGORY = "Category"

How to test
===========

     export PYTHONPATH=./
     pytest


