from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)


label1=Label(root, text="메뉴선택").pack()

# radio= 여러개 항목중 선택
burger_var=IntVar()
btn_burger1=Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2=Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3=Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2=Label(root, text="음료선택").pack()
drink_var=StringVar()
btn_drink1=Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2=Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
def btncmd():
    print(burger_var.get())
    print(drink_var.get())
bt1=Button(root, text="주문", command=btncmd)
bt1.pack()

root.mainloop()