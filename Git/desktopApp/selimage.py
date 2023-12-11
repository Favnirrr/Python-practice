import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImg = PIL.Image.open(path).convert("L").resize((32,32)).resize((300,300),resample=0)
    imgData = PIL.ImageTk.PhotoImage(newImg)
    imgLbl.configure(image = imgData)
    imgLbl.image = imgData

def openFile():
    path = fd.askopenfilename()
    if path:
        dispPhoto(path)
    

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く",command=openFile)
imgLbl = tk.Label()

btn.pack()
imgLbl.pack()

tk.mainloop()