from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)

frame= Frame(root)
frame.pack()

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
# set이 없으면 스크롤을 내려도 다시 올라옴
listbox=Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
# 리스트box와 scrollbar간에 서로 매핑해야함

for i in range(1,32):
    listbox.insert(END,str(i)+"일")

scrollbar.config(command=listbox.yview)
listbox.pack(side="left")
def btncmd():
    print(listbox.curselection())
btn=Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()