# 手書き文字を判定しよう
これはPython講義のデモアプリの1つで、 Pythonで機械学習を行う練習課題です.  
手書きで0〜9のいずれかの数値を書くと、それが何かを判定して画面に表示します.
***
![手書き文字を判定しよう](https://raw.githubusercontent.com/yoheimune-python-lecture/hand-written-digit-recognition/image/resources/screenshot.png)
[デモはこちら](http://demo-digit-recognition.paint-ink.com/)  

# フォルダ構成
`blank` ディレクトリには演習を通して実装するためのほぼ空っぽの内容があり、
`answer` ディレクトリには完成品が入っています。

# 演習の準備
以下の手順で演習を進めてください。
## リポジトリの取得
リポジトリからプログラムコード一式をダウンロードしてください。
## 必要ライブラリのインストール
利用するライブラリを `pip`でインストールします.  
Macの場合 `pip3` コマンド、Windowsの場合 `pip` コマンドを実行します.
```
# Windowsの場合
pip install --upgrade flask
pip install --upgrade numpy
pip install --upgrade matplotlib
pip install --upgrade scipy
pip install --upgrade scikit-learn

# Macの場合
pip3 install --upgrade flask
pip3 install --upgrade numpy
pip3 install --upgrade matplotlib
pip3 install --upgrade scipy
pip3 install --upgrade scikit-learn
```
