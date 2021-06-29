# 메모장 따라만들기
# 현재기능:
# 저장, 열기, 새창, 다른이름으로 저장
# 저장시 텍스트나 파이썬 파일 아니면 자동 txt파일로 저장
# 새창시 무조건 다른이름저장
# 실행취소, 찾기(text.tag 이용) but 창 이동 해야 블록 보임

# 구현할것(편집탭)

# 텍스트창 꽉채우기( 창크기에따라)
# 디렉토리 이동
# 

# UI를 클래스로 구분해서 따로 작성해야게씀
# 파일 이름은 entry로

import tkinter.messagebox as msgbox
from tkinter import *
import os

# 경로
current_path=os.path.join(os.path.dirname(__file__),"folder")
print(current_path)
# 메모장 화면
root=Tk()
root.title("제목 없음")
root.geometry("480x480")
root.resizable(True, True)

is_newtap=True  
# 처음 켰을때 새 창이다.
# title이 제목 없음 이라도 이름이 *로되어있고 저장불가능 이름임. 저장시 이름 직접 작성해야함

# 파일 열기 화면
class UI_fileopen:
    def __init__(self):
        global is_newtap
        self.UI_open=Toplevel(root)
        self.UI_open.title("열기")
        self.UI_open.geometry("480x300")
        self.UI_open.resizable(True, True)
        self.file_list = os.listdir(current_path)    # 디렉토리내 파일 리스트
        self.listbox=Listbox(self.UI_open, selectmode="single",width=40, height=10)
        for file_name in self.file_list:
            self.listbox.insert(END, file_name)
        self.listbox.pack(side="top")
        self.file_name_txt=Entry(self.UI_open, width=50)
        self.file_name_txt.pack(side="left")
        self.btn_open=Button(self.UI_open, text="열기", command=self.load_text)
        self.btn_cancel=Button(self.UI_open, text="취소", command=self.UI_open.destroy)
        self.btn_cancel.pack(side="right")
        self.btn_open.pack(side="right")
        # 리스트박스 선택시 동작 bind
        self.listbox.bind("<<ListboxSelect>>", self.get_file_name)    # 리스트박스 선택시
        self.UI_open.mainloop()

    def load_text(self):
        global is_newtap
        # if self.listbox.curselection():
        #     file_name=self.listbox.get(self.listbox.curselection())
        file_name=self.file_name_txt.get()
        if file_name:
            try:
                f=open(os.path.join(current_path,file_name), "r", encoding="UTF-8")
            except:
                msgbox.showerror("error", "존재하지 않는 파일입니다.")
            else:
                data=f.read()[:-1]  # 마지막에 \n가 기입돼서 지워줌
                # 메인 ui에서 동작하게 해야함
                is_newtap=False
                txt.delete("1.0", END)
                txt.insert("1.0",data)
                root.title(file_name)
                self.UI_open.destroy()
                cancel(self)

    def get_file_name(self, event):
        widget = event.widget   # 현재 이벤트의 위젯정보 (listbox)
        file_name=widget.get(widget.curselection())
        self.file_name_txt.delete(0, END)
        self.file_name_txt.insert(0,file_name)
    
    def __del__(self):
        self.UI_open.destroy()


# 저장 UI
# 새창이면 파일이름 * => 파일이름 작성해서 저장
# 새창아니면 내용만 저장

class UI_filesave:
    def __init__(self):
        global is_newtap
        self.UI_save=Toplevel(root)
        self.UI_save.title("열기")
        self.UI_save.geometry("480x300")
        self.UI_save.resizable(True, True)
        self.file_list = os.listdir(current_path)    # 디렉토리내 파일 리스트
        self.listbox=Listbox(self.UI_save, selectmode="single",width=40, height=10)
        for file_name in self.file_list:
            self.listbox.insert(END, file_name)
        self.listbox.pack(side="top")
        self.file_name_txt=Entry(self.UI_save, width=50)
        self.file_name_txt.pack(side="left")
        self.btn_open=Button(self.UI_save, text="저장", command=self.save_text)
        self.btn_cancel=Button(self.UI_save, text="취소", command=self.UI_save.destroy)
        self.btn_cancel.pack(side="right")
        self.btn_open.pack(side="right")
        # 리스트박스 선택시 동작 bind
        self.listbox.bind("<<ListboxSelect>>", self.get_file_name)    # 리스트박스 선택시

        # 파일이름 작성란
        if is_newtap:
            self.file_name_txt.delete(0,END)
            self.file_name_txt.insert(0, "*.txt")
        else:
            self.file_name_txt.delete(0,END)
            self.file_name_txt.insert(0, f"{root.title()}")

        self.UI_save.mainloop()
    # 파일이름 가져오기
    def get_file_name(self, event):
        widget = event.widget   # 현재 이벤트의 위젯정보 (listbox)
        file_name=widget.get(widget.curselection())
        self.file_name_txt.delete(0, END)
        self.file_name_txt.insert(0,file_name)

    # 저장
    def save_text(self):
        global is_newtap
        file_name=self.file_name_txt.get()
        name1,name2=os.path.splitext(file_name)
        # 확장자가 텍스트나 파이썬 파일이 아니면 txt파일로 자동저장
        if name2!=".txt" and name2!=".py":
            file_name=file_name+".txt"
        try:
            f=open(os.path.join(current_path,file_name), "w", encoding="UTF-8")
        except:
            msgbox.showerror("error", "올바른 파일 이름입력.")
        else:
            is_newtap=False
            root.title(file_name)
            data=txt.get("1.0", END)
            f.write(data)
            f.close
            self.UI_save.destroy()
            cancel(self)
    
    def __del__(self):
        self.UI_save.destroy()



# 찾기 UI
class UI_find:
    def __init__(self):
        self.UI=Toplevel(root)
        self.UI.title()
        self.UI.geometry("200x50")
        self.frame=Frame(self.UI)
        self.frame.pack(fill="both")
        self.UI.resizable(False, False)
        self.entry=Entry(self.frame)
        self.btn_find=Button(self.frame,text="찾기", command=self.find)
        self.entry.pack(side="left")
        self.btn_find.pack(side="right")
        self.start="1.0"
        self.UI.mainloop()

    
    def find(self):
        # 기존 블록처리된거 없에기
        txt.tag_remove("sel", "1.0", END)
        self.start=txt.index(INSERT)
        word=self.entry.get()
        pos = txt.search(word, self.start, stopindex=END)
        if not pos:
            self.start="1.0"
            pos = txt.search(word, self.start, stopindex=END)
            if not pos:
                msgbox.showerror("에러", "찾는 단어가 없습니다.")
                return
        length = len(word)
        row, col = pos.split('.')
        end = int(col) + length
        end = row + '.' + str(end)
        print(end)

        # 블럭처리 해줌(드래그된 상태)
        # 블럭처리 되면 커서도 블럭처리된 글자 앞으로이동
        # insert마크를 가져와야 글자삽입 마크를 가져온다
        txt.tag_add("sel", pos, end)
        txt.mark_set(INSERT,SEL_LAST)
        root.update()
        self.start=end




def cancel(UI):
    del UI


# 메뉴함수

# 파일메뉴 함수
# 오픈시 저장여부
def yesnocancel():
    response=msgbox.askyesnocancel(title="변경 저장", message=f"변경내용을 저장하시겠습니까?")
    return response
    # 예=1 아니오=0 취소=-1

# 변화 내용을 감지해서 저장할지 물어봄
def check_save():
        
    file_list = os.listdir(current_path)
    if file_list.count(root.title()): # 현재 제목을 가진 파일이 있는지 확인
        f=open(os.path.join(current_path,root.title()), "r", encoding="UTF-8")
        data=f.read()
        f.close()
    else:
        data="\n"   # \n 으로 해야 공백 text박스와 일치
    # 현재 파일 내용이 원본과 다르면
    # 저장할지 여부 묻기
    if txt.get("1.0", END)!=data:
        res=yesnocancel()
        if res==1:  # 예: 저장
            f_save=open(os.path.join(current_path,root.title()), "w", encoding="UTF-8")
            data=txt.get("1.0", END)
            f_save.write(data)
            f_save.close()
            return 1
        elif res==0:    # 아니오
            return 0
        else:   # 취소
            return -1
    else:   # 변경내용 없으면 return 1
        return 1
def open_file():
    if check_save() != -1:
        UI=UI_fileopen()

def save_file():
    # 새 창일경우 파일이름 설정
    if is_newtap:
        UI=UI_filesave()

    else:
        f=open(os.path.join(current_path,root.title()), "w", encoding="UTF-8")
        data=txt.get("1.0", END)
        f.write(data)
        f.close
# 끝내기
def cmd_quit():
    if check_save() !=-1:
        root.quit()

# 새창
def new_tap():
    if check_save()==-1:
        return
    global is_newtap
    is_newtap=True
    root.title("제목 없음")
    txt.delete("1.0", END)

# 다른이름으로 저장
def save_as():
    UI=UI_filesave()

# 편집메뉴 함수
def find_word():
    UI=UI_find()

# 메뉴
menu=Menu(root)
menu_file=Menu(menu, tearoff=0)
menu_edit=Menu(menu, tearoff=0)
menu_text=Menu(menu, tearoff=0)
menu_view=Menu(menu, tearoff=0)
menu_help=Menu(menu, tearoff=0)
# 메뉴 파일
menu_file.add_command(label="새 창", command=new_tap)
menu_file.add_separator()
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_command(label="다른 이름으로 저장", command=save_as)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=cmd_quit)

menu.add_cascade(label="파일", menu=menu_file)
# 메뉴 편집
menu_edit.add_command(label="찾기", command=find_word)
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
txt=Text(frame,yscrollcommand=scrollbar.set, endline=None)  # 사이즈 비우니 전체가 text로 됨 but 사이즈 바꿔도 텍스트박스 크기고정;
txt.pack(side="left",fill="both", expand=True)
# txt.grid(row=0, column=0, sticky=N+W+S+E)
scrollbar.config(command=txt.yview)



root.config(menu=menu)
root.mainloop()
