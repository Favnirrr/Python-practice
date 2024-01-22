import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImg = PIL.Image.open(path).convert("L").resize((8,8)).resize((300,300),resample=0)
    imgData = PIL.ImageTk.PhotoImage(newImg)
    imgLbl.configure(image = imgData)
    imgLbl.image = imgData

def openFile():
    path = fd.askopenfilename()
    if path:
        dispPhoto(path)

#   def savePhoto(path):
#   # 画像を保存する
#   if newImg:
#   newImg.save(path, quality=95)

#   def saveFile():
#       path = fd.asksaveasfilename()
#       print(path)
#       if path:
#           savePhoto(path)

#   newImg = None

root = tk.Tk()
root.geometry("400x350")

btn_openFile = tk.Button(text="ファイルを開く",command=openFile)
#   btn_saveFile = tk.Button(text="画像を保存",command=saveFile)
imgLbl = tk.Label()

btn_openFile.pack()
#   btn_saveFile.pack()
imgLbl.pack()

tk.mainloop()
