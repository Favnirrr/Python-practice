import os
from sklearn import datasets, svm
import joblib
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk


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
    if not os.path.exists(DIGITS_PKL):
        clf = train_digits()
    clf = joblib.load(DIGITS_PKL)
    # 予測する
    n = clf.predict([data])
    print(data)
    print("判定結果=", n)
    # 画面に表示する
    root.title("判定結果=" + str(n))
    ans_Label.configure(text="判定結果 = " + str(n))

def dispPhoto(path):
    import numpy as np
    from PIL import Image
    
    # 取得画像をリサイズ
    image = PIL.Image.open(path).convert("L").resize((8,8), Image.Resampling.LANCZOS)
    imgData = image
    imgData = PIL.ImageTk.PhotoImage(imgData.resize((300,300),resample=0))
    imgLbl.configure(image = imgData)
    imgLbl.image = imgData
    
    img = np.asarray(image, dtype=float)
    img = np.floor(16 - 16 * (img / 256)) # 行列演算
    img = img.flatten()
    return img

def openFile():
    path = fd.askopenfilename()
    if path:
        data = dispPhoto(path)
        predict_digits(data)

# -----------------------------------

# 結果を格納する変数

root = tk.Tk()
root.geometry("400x400")

btn_openFile = tk.Button(text="ファイルを開く",command=openFile)
imgLbl = tk.Label()

# 判定結果を表示する数値を表示
# 大きさを変更するために、font=("Helvetica", 20)
ans_Label = tk.Label(font=("Helvetica", 20))


btn_openFile.pack()
#   btn_saveFile.pack()
imgLbl.pack()
ans_Label.pack()

tk.mainloop()
