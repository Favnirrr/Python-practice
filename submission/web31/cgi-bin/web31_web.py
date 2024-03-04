import os
from sklearn import datasets, svm
import joblib
import PIL.Image
import PIL.ImageTk
import cgi
import cgitb
import io
import numpy as np
import base64

# モデルデータファイル名 現在の階層に作成
DIGITS_PKL = "digits.pkl"

# 予測モデルを作成する
def train_digits():
    # 手書き数字データを読み込む
    digits = datasets.load_digits()
    # 訓練する
    data_train = digits.data
    label_train = digits.target
    clf = svm.SVC(gamma=0.001)
    clf.fit(data_train, label_train)
    # 予測モデルを保存する
    joblib.dump(clf, DIGITS_PKL)
    print("予測モデルを保存しました=", DIGITS_PKL)
    return clf

# データから数字を予測する
def predict_digits(data):
    # モデルファイルを読み込む
    clf = joblib.load(DIGITS_PKL)
    # 予測する
    n = clf.predict([data])
    result_html = '<p>answer = <strong>{}</strong></p>'.format(n)
    # 画面に表示する
    print('<script>document.getElementById("ansLabel").innerHTML = "{}";</script>'.format(result_html))

# アップロードされたファイルをバイトデータに変換する
def dispPhoto(data):
    # ファイルが正しくバイトデータに変換されているか確認
    if isinstance(data, bytes):
        # 取得画像をリサイズ
        image = PIL.Image.open(io.BytesIO(data)).convert("L").resize((8, 8), PIL.Image.Resampling.LANCZOS)

        # PILのImageをbase64エンコードしてHTMLに表示
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("utf-8")
        print('<script>document.getElementById("imgLbl").src = "{}";</script>'.format(img_str))

        img = np.asarray(image, dtype=float)
        img = np.floor(16 - 16 * (img / 256))  # 行列演算
        img = img.flatten()

        return img
    else:
        print("File was not converted correctly.")

def openFile(img):
    # ファイルがアップロードされているか確認
    if img:
        data = dispPhoto(img)
        predict_digits(data)
    else:
        print("no file uploaded.")

# Webアプリケーションフレームワーク
# 画像ファイルをアップロードし、数字を判定する

if not os.path.exists(DIGITS_PKL):
    train_digits()

# ブラウザデバッグ有効化
cgitb.enable()

# HTMLを画面に表示する
# ヘッダを出力
print("Content-Type: text/html; charset=utf-8")
print("")
# HTMLを出力
print("""
<html>
<head>
    <meta charset="utf-8">
    <title>digit detect</title>
</head>
<body>
    <h2>digit detect</h2>
    <form name="fm" action="app31_web.py" method="post" enctype="multipart/form-data">
        <input type="file" id="imagefile" name="imgfile">
        <input type="submit" value="enter">
    </form>
    <br>
    <img id="imgLbl" src="" width="300" height="300">
    <br>
    <p id="ansLabel"></p>
</body>
</html>
""")

form = cgi.FieldStorage()
postedImg = form.getvalue("imgfile") 
openFile(postedImg)
