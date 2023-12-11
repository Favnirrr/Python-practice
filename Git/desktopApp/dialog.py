# 208,209,211p
import tkinter as tk # 208p デスクトップアプリとは 参照
import random

root = tk.Tk()
root.geometry("200x100")

def omikuji():
    omikuji = ["大吉","中吉","小吉","凶"]
    # ランダム
    
    lbl.configure(text=random.choice(omikuji))

lbl =  tk.Label(text="label")
btb = tk.Button(text="Push" , command = omikuji)

lbl.pack()
btb.pack()

tk.mainloop()  