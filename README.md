# チケット自動購入BOT

## 導入方法
1. ツールのダウンロード
2. phtonのインストール
3. Seleniumのインストール
4. ドライバのインストール
5. 必要なジュールをインストール

### ツールのダウンロード

### pythonのインストール
1. lib/python/にあるpython-3.8.5-amd64.exeを起動する。
2. Install Nowを選択してインストールを開始する前ににAdd Python 3.8 to PATHにチェックを入れる
3. Install Nowをクリックしてインストール開始
4. Windowsのコマンドプロンプトを起動し以下のコマンドでインストールの確認
   > python -V  
   Python 3.8.2

### Seleniumのインストール
1. コマンドプロンプトを開き、pipでseleniumをインストール。
   >pip install selenium

### ドライバのインストール
1. Google Chromeeのインストール(インストールされている場合はスキップ)
   >https://www.google.co.jp/chrome/?brand=CHBD&gclid=EAIaIQobChMIw_WEyJD66wIVwVBgCh2TagCmEAAYASAAEgL94vD_BwE&gclsrc=aw.ds
2. Chromeのドライバをインストール
   >pip install chromedriver_binary==85.0.4183.87.0

### 必要なモジュールをインストール
1. 以下のパスにある.batファイルを起動する
   >./init/init.bat


## 使い方