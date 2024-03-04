import tkinter.filedialog as fd

import cgi
import cv2
import numpy as np

form = cgi.FieldStorage()

# ヘッダの表示
print("Content-Type: text/html; charset=utf-8")
print("")

# すべてのパラメータを取得して表示
print("--- all params ---")

path = fd.askopenfilename(
    title = "処理対象のファイルを指定してください",
    filetypes = [("PNG", ".png"), ("JPEG", ".jpg")]
)

# ----------------------------------------

if "imagefile" in form:
    img = form.getvalue("imagefile")
    arr  = np.asarray(
        bytearray(img),
        dtype = np.uint8
    )
    
    d_img = cv2.imdecode(arr, -1)
    cv2.imwrite("numimage.png", d_img)
    print("<img src='../numimage.png'>")