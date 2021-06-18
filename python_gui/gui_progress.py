import tkinter.ttk as ttk
from tkinter import *
import time

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)


# progressbar=ttk.Progressbar(root, maximum=100, mode="indeterminate")   # 왔다갔다
# #progressbar=ttk.Progressbar(root, maximum=100, mode="determinate")  # 게이지 차는거
# progressbar.start(10)   # 10ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop()
# btn=Button(root, text="선택", command=btncmd)
# btn.pack()

p_var2=DoubleVar()   # 실수값 보기위해
progressbar2=ttk.Progressbar(root, maximum=200, length=150, variable=p_var2)
progressbar2.pack()


def btn_start():
    for i in range(101):
        time.sleep(0.01)

        p_var2.set(i)   # progressbae 값설정
        progressbar2.update()   # gui업데이트
        print(p_var2.get())

btn=Button(root, text="시작", command=btn_start)
btn.pack()

root.mainloop()