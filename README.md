# チケット自動購入BOT

## 導入方法
1. ツールのダウンロード
2. phtonのインストール
3. Seleniumのインストール
4. ドライバのインストール
5. 必要なジュールをインストール

### ツールのダウンロード
1. ブラウザから以下のURLを開く
   >https://github.com/chigirh/ticket-buy-tool
2. 右上にある「Code」と書かれているボタンをクリックする。
3. Download ZIPをクリックしてZipファイルをダウンロードする。
4. ダウンロードしたフィイルを解凍して任意の場所にコピーする。
   >解凍方法が分からなければ以下参照  
   https://www.yurikago.net/yurietax/unzip_vista7.html#:~:text=%E3%83%80%E3%82%A6%E3%83%B3%E3%83%AD%E3%83%BC%E3%83%89%E3%81%97%E3%81%9Fzip%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92,%E5%B1%95%E9%96%8B%E3%80%8D%E3%82%92%E9%81%B8%E6%8A%9E%E3%81%97%E3%81%BE%E3%81%99%E3%80%82&text=%E3%80%8C%E5%9C%A7%E7%B8%AE%EF%BC%88%EF%BC%BA%EF%BC%A9%EF%BC%B0%E5%BD%A2%E5%BC%8F%EF%BC%89%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%83%BC,%E5%B1%95%E9%96%8B%E3%80%8D%E3%82%92%E9%81%B8%E6%8A%9E%E3%81%97%E3%81%BE%E3%81%99%E3%80%82&text=%E5%9C%A7%E7%B8%AE%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%82%92%E8%A7%A3%E5%87%8D%E3%81%97%E3%81%9F%E3%83%95%E3%82%A9%E3%83%AB%E3%83%80%E3%81%8C%E5%87%BA%E6%9D%A5%E4%B8%8A%E3%81%8C%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82

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
2. コマンドプロンプトを開き、Chromeのドライバをインストール
   >pip install chromedriver_binary==85.0.4183.87.0

### 必要なモジュールをインストール
1. 以下のパスにある.batファイルを起動する
   >./init/init.bat


## 使い方

###　設定ファイルの作成
1. index.htmlをダブルクリック
2. チケット購入に必要な情報を記入する。
   - ログインページのURL:ログインページのURL(https://t.livepocket.jp/loginのままで良い)
   - チケット購入ページのURL:購入したいチケットの購入ページのURL(例:https://t.livepocket.jp/e/chula_neco0927)
   - ログインメールアドレス:ログイン時に利用する自分のメールアドレス
   - パスワード:ログイン時に利用するパスワード
   - 発売開始時刻:購入したいチケットの販売開始時刻(例:21時ちょうどに販売開始の場合は21:00:00と入力)
   - チケット種別:購入したいチケットの種別を選択(チケット購入ページの購入したいチケット種別の上からの番号を選択する)※チケット購入ページに存在しない番号は選択しないこと
   - 購入したい枚数を選択する。※チケット購入ページに存在しない枚数は選択しないこと
   - 支払いをするコンビニを選択:振り込みを行うコンビニを選択
3. 保存ボタンをクリック
4. 保存されたconf.jsonファイルをindex.htmlと同じフォルダにコピー
   
### 実行
1. execute.batを実行