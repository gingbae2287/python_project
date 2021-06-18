import tkinter.ttk as ttk
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)

values=[str(i)+"일" for i in range(1,32)]
# combobox= 리스트를 내릴수 있음
combobox=ttk.Combobox(root, height=10, values=values, state="readonly")
combobox.set("카드결제일")  # 최초 목록의 제목
combobox.current(0)
combobox.pack()

def btncmd():
    print(combobox.get())
btn=Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()