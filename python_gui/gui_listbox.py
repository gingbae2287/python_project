from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)

listbox=Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨뒤항목 삭제 or 숫자입력
    # 갯수확인
    #print("리스트에는", listbox.size(), "개가있어요")
    # 항목확인
    #print("1번쨰 부터 3번째 까지항목: ", listbox.get(0,2))

    # 선택된 항목 확인 return idx tuple
    print("선택: ", listbox.curselection()) #current selection
bt1=Button(root, text="클릭", command=btncmd)
bt1.pack()

root.mainloop()