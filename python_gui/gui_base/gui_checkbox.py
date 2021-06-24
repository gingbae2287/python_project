from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)

chkvar=IntVar() # chkvar에 int형으로 값을 저장
chkbox=Checkbutton(root, text="오늘하루 보지않기", variable=chkvar)
# chkbox.select() # 자동 선택처리
# chkbox.deselect()   # 선택 해제 처리

chkbox.pack()

chkvar2=IntVar()
chkbox2=Checkbutton(root, text="일주일 동안 보지않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get(), chkvar2.get())
bt1=Button(root, text="클릭", command=btncmd)
bt1.pack()

root.mainloop()