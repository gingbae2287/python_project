from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)

Label(root, text="메뉴선택").pack(side="top")
Label(root, text="주문하기").pack(side="bottom")
frame_buger=Frame(root, relief="solid", bd=2)
frame_buger.pack(side="left", fill="both", expand=True)

Button(frame_buger, text="햄버거").pack()

Button(frame_buger, text="치즈버거").pack()

Button(frame_buger, text="치킨버거").pack()

frame_drink=LabelFrame(root, text="음료", bd=5)
frame_drink.pack(side="right",fill="both",expand=True)
Button(frame_drink, text="콜라").pack()

Button(frame_drink, text="사이다").pack()

Button(frame_drink, text="환타").pack()


root.mainloop()