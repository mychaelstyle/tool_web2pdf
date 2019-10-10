tool_web2pdf
============

MacOS上でExcelに書かれたWebページURLのリストからChromeのコマンドラインheadlessから実行して指定のフォルダにPDFで保存します。

Webアプリケーションで表示している指定の大量の詳細ページを3000以上を来週までにPDF化して印刷屋に回せるようにnnnnn.pdfのような規則正しい名前でPDF出力できるようにしてくれなどの指示が突然降ってきてお困りのあなたに最適な簡単なスクリプトです。

Environment
===========

- Mac OS X 10.14.6
- python >= 3.7
- anaconda3-2019.03
- Google Chrome 77.0.3865.90 (Official Build)

How to use
===========

Excelのフォーマット
------------------

一行目をラベル名とし、二行目から実行されます。
ファイル名にしたい列のラベルを ID としてください。
アクセスしてPDF化したいURLラベルを URL としてください。

サンプルはtext/fixtures/data.xlsxの内容をみてください。

実行方法
--------
ターミナルを起動してクローンしたフォルダの中に移動し、下記のコマンドを実行してください。

    python make.py [excel file path] [excel sheet name] [output folder path]

How to use on another OS
========================

make.pyの4行目,以下の行のChromeコマンドのパスを自分の環境のパスに書き換えて実行してください。

    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


