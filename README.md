tool_web2pdf
============

MacOS上でExcelに書かれたWebページURLのリストからChromeのコマンドラインheadlessから実行して指定のフォルダにPDFで保存するスクリプトのテスト。

How to use
===========

Excelの列は,A列=保存したいPDFファイル名, B列=名前, C列=URLのフォーマットで用意します。
一行目はラベル行として読み込みません。
サンプルはtext/fixtures/data.xlsxの内容をみてください。

    python make.py [excel file path] [excel sheet name] [output folder path]

How to use on another OS
========================

make.pyの4行目,以下の行のChromeコマンドのパスを自分の環境のパスに書き換えて実行してください。

    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


