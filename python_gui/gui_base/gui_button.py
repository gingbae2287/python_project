from tkinter import *

root=Tk()
root.title("GUI")
# root.geometry("480x480") 가로x세로
root.geometry("480x480+400+100")
root.resizable(False, True) # 사이즈 조절 가로,세로 가능여부

bt1=Button(root, text="버튼1")
bt1.pack()  # 버튼 보이게

bt2=Button(root,padx=5, pady=10, text="버튼222222222")  # pad 글자 양옆 공간
bt2.pack()

bt3=Button(root,padx=10, pady=10, text="버튼3")
bt3.pack()

bt4=Button(root, width=10, height=3, text="버튼444444444444444444ㄴ")   # width, height 는 버튼사이즈, 글자 잘릴수도있음
bt4.pack()
# fg는 폰트색 bg는 배경색
bt5=Button(root, fg="red", bg="yellow", text="버튼5")
bt5.pack()

check_button=PhotoImage(file="check_button.png")
bt6=Button(root, image=check_button)
bt6.pack()

def btncmd():
    print("버튼이 클릭돼써염")
bt7=Button(root, text="동작", command=btncmd)
bt7.pack()

root.mainloop()
