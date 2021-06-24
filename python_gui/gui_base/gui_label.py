from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")

label1=Label(root, text="안녕하세요")
label1.pack()

check_button=PhotoImage(file="gui_base/check_button.png")
label2=Label(root, image=check_button)
label2.pack()

def change():
    label1.config(text="바꿔")
    # garbege collection 불필요한 메모리 공간 해제
    global x_button
    x_button=PhotoImage(file="gui_base/x_button.png")
    label2.config(image=x_button)
    
bt1=Button(root, text="클릭", command=change)
bt1.pack()

root.mainloop()