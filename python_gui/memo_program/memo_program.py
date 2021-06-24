import tkinter.messagebox as msgbox
from tkinter import *
import os

# 경로
current_path=os.path.dirname(__file__)
# 메모장 화면
root=Tk()
root.title("제목 없음")
root.geometry("480x480")
root.resizable(True, True)

# 파일 열기 화면
# UI_open=Toplevel()
# UI_open.title("열기")
# UI_open.geometry("480x200")
# UI_open.resizable(True, True)
# listbox=Listbox(UI_open, selectmode="single")

# 파일 불러오기
def load_text(listbox, UI):
    if listbox.curselection():
        file_name=listbox.get(listbox.curselection())
        f=open(f"memo_program/{file_name}", "r", encoding="UTF-8")
        data=f.read()[:-1]  # 마지막에 \n가 기입돼서 지워줌
        txt.delete("1.0", END)
        txt.insert("1.0",data)
        root.title(file_name)
        UI.destroy()
    else:
        msgbox.showerror("error", "파일을 선택하세요.")

def Open_UI():
    UI_open=Toplevel(root)
    UI_open.title("열기")
    UI_open.geometry("480x200")
    UI_open.resizable(True, True)
    file_list = os.listdir(current_path)    # 디렉토리내 파일 리스트

    listbox=Listbox(UI_open, selectmode="single")
    for file_name in file_list:
        listbox.insert(END, file_name)
    listbox.pack(side="left")
    btn_open=Button(UI_open, text="열기", command=lambda: load_text(listbox, UI_open))
    btn_cancel=Button(UI_open, text="취소", command=UI_open.destroy)
    btn_cancel.pack(side="right")
    btn_open.pack(side="right")
    UI_open.mainloop()



# 메뉴

menu=Menu(root)
menu_file=Menu(menu, tearoff=0)
menu_edit=Menu(menu, tearoff=0)
menu_text=Menu(menu, tearoff=0)
menu_view=Menu(menu, tearoff=0)
menu_help=Menu(menu, tearoff=0)

# 오픈시 저장여부
def yesnocancel():
    response=msgbox.askyesnocancel(title="변경 저장", message=f"변경내용을 저장하시겠습니까?")
    return response
    # 예=1 아니오=0 취소=-1

# 변화 내용을 감지해서 저장할지 물어봄
def check_save():
    file_list = os.listdir(current_path)
    if file_list.count(root.title()): # 현재 제목을 가진 파일이 있는지 확인
        f=open(f"memo_program/{root.title()}", "r", encoding="UTF-8")
        data=f.read()
        f.close()
    else:
        data="\n"   # \n 으로 해야 공백 text박스와 일치
    # 현재 파일 내용이 원본과 다르면
    # 저장할지 여부 묻기
    if txt.get("1.0", END)!=data:
        res=yesnocancel()
        if res==1:  # 예: 저장
            f_save=open(f"memo_program/{root.title()}", "w", encoding="UTF-8")
            data=txt.get("1.0", END)
            f_save.write(data)
            f_save.close()
            return 1
        elif res==0:    # 아니오
            return 0
        else:   # 취소
            return -1
def open_file():
    if check_save() != -1:
        Open_UI()

def save_file():
    f=open(f"memo_program/{root.title()}", "w", encoding="UTF-8")
    data=txt.get("1.0", END)
    f.write(data)
    f.close
# 끝내기
def cmd_quit():
    if check_save() !=-1:
        root.quit()

menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=cmd_quit)


menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_text)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)


# 프레임
frame= Frame(root)
frame.pack(fill="both", expand=True)


# 본문 텍스트 박스

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
txt=Text(frame, padx=0, pady=0,yscrollcommand=scrollbar.set, endline=None)  # 사이즈 비우니 전체가 text로 됨 but 사이즈 바꿔도 텍스트박스 크기고정;
txt.pack(side="left", )
# txt.grid(row=0, column=0, sticky=N+W+S+E)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()