# 메모장 따라만들기
# 현재기능:
# filedialog 사용 안하고 구현했다
# 저장, 열기(더블클릭으로도), 새창, 다른이름으로 저장
# 저장시 텍스트나 파이썬 파일 아니면 자동 txt파일로 저장
# 새창시 무조건 다른이름저장
# 실행취소(text.edit_undo), 찾기, 바꾸기, 모두바꾸기(블록있으면 블록안에서만)
# 찾기에 단어(2자이상) 입력시 바로바로 모든 단어 블록처리(선택단어는 색 찐하게 블록)
# 단축키 넣음
# 파일탐색 UI에서 디렉토리이동(이전폴더, 폴더 들어가기 가능)

# 실행취소 undo가 시원찮아서 방법을 찾아야함. (파일 로드된것도 실행취소하면 텍스트만 지워버림;)
# 버퍼?

# 구현할 것 (파일탭)

# 구현할것(편집탭)
# 모두 바꾸기 바뀐 단어에 다 블록처리
# (파일열기)디렉토리 이동 => tkinter.filedialog 를 쓰면 구현돼있어서 쉽지만
# 일단 os를 이용해 구현해 보겠음



import tkinter.messagebox as msgbox
from tkinter import *
import os
from UI_file import *

# 경로
# current_path=os.path.join(os.path.dirname(__file__),"folder")

# # #########
# dir_list=current_path.split("\\")



######

# 메모장 화면
root=Tk()
root.title("제목 없음")
root.geometry("480x480")
root.resizable(True, True)

# 프레임
frame= Frame(root)
frame.pack(fill="both", expand=True)


# 본문 텍스트 박스

scrollbar=Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
txt=Text(frame,yscrollcommand=scrollbar.set, endline=None, inactiveselectbackground="blue", undo=True, autoseparators=True )  # 사이즈 비우니 전체가 text로 됨 but 사이즈 바꿔도 텍스트박스 크기고정;
txt.pack(side="left",fill="both", expand=True)
# txt.grid(row=0, column=0, sticky=N+W+S+E)
scrollbar.config(command=txt.yview)

is_newtap=True  
# 처음 켰을때 새 창이다.
# title이 제목 없음 이라도 이름이 *로되어있고 저장불가능 이름임. 저장시 이름 직접 작성해야함

class UI_open(UI_file):
    def __init__(self,root):
        super().__init__(root)
        
        
        self.btn_open=Button(self.frame_bottom, text="열기", command=self.open)
        self.btn_open.grid(row=0,column=1)
        
        self.list_files.bind("<Double-Button-1>", self.open)
        self.UI.mainloop()

    def open(self,event=None):
        global is_newtap
        
        file_name=self.file_name_txt.get()
        if not file_name:
            msgbox.showerror("error", "폴더 또는 파일명을 입력하세요.")
            return
        # 파일인지 폴더인지 판단
        tmp_path=os.path.join(get_cur_path(),file_name)
        if os.path.isdir(tmp_path): # 폴더
            self.go_path(tmp_path)
        else:
            try:
                f=open(os.path.join(get_cur_path(),file_name), "r", encoding="UTF-8")
            except:
                msgbox.showerror("error", "파일을 열 수 없음.")
            else:
                data=f.read()[:-1]  # 마지막에 \n가 기입돼서 지워줌
                # 메인 ui에서 동작하게 해야함
                is_newtap=False
                txt.delete("1.0", END)
                txt.insert("1.0",data)
                root.title(file_name)
                self.UI.destroy()

# 저장 UI
# 새창이면 파일이름 * => 파일이름 작성해서 저장
# 새창아니면 내용만 저장

class UI_save(UI_file):
    def __init__(self,root):
        super().__init__(root)
        self.btn_save=Button(self.frame_bottom, text="저장", command=self.save_text)
        self.btn_save.grid(row=0,column=1)

        if is_newtap:
            self.file_name_txt.delete(0,END)
            self.file_name_txt.insert(0, "*.txt")
        else:
            self.file_name_txt.delete(0,END)
            self.file_name_txt.insert(0, f"{root.title()}")

        self.UI.mainloop()

    def save_text(self):
        global is_newtap
        file_name=self.file_name_txt.get()
        name=os.path.splitext(file_name)[1]
        # 확장자가 텍스트나 파이썬 파일이 아니면 txt파일로 자동저장
        if name!=".txt" and name!=".py":
            file_name=file_name+".txt"
        try:
            f=open(os.path.join(get_cur_path(),file_name), "w", encoding="UTF-8")
        except:
            msgbox.showerror("error", "올바른 파일 이름입력.")
        else:
            is_newtap=False
            root.title(file_name)
            data=txt.get("1.0", END)
            f.write(data)
            f.close
            self.UI.destroy()


# 찾기 UI
class UI_find:
    def __init__(self):
        self.UI=Toplevel(root)
        self.UI.title()
        self.UI.geometry("400x200")
        self.UI.resizable(False, False)

        # 창 종료 호출되면 콜백될 함수.
        # destroy도 써줘야함
        self.UI.protocol("WM_DELETE_WINDOW", self.destroy_window)

        self.entry=Entry(self.UI)
        self.entry_change=Entry(self.UI)
        self.btn_find=Button(self.UI,text="찾기", command=self.find)
        self.btn_change=Button(self.UI, text="바꾸기", command=self.change)
        self.btn_changeall=Button(self.UI, text="모두 바꾸기", command=self.change_all)

        self.entry.grid(row=0, column=0)
        self.entry_change.grid(row=1, column=0)
        self.btn_find.grid(row=0, column=1,sticky=N+E+W+S)
        self.btn_change.grid(row=1, column=1,sticky=N+E+W+S)
        self.btn_changeall.grid(row=2, column=1,sticky=N+E+W+S)

        # 찾기에 텍스트 입력시 실시간으로 블록해줌
        # UI나 frame에 바인드해야 블록이 바로바로 업데이트댐
        self.UI.bind("<Key>", self.find_key)

        self.UI.mainloop()

    # 키 바인드 될때마다 실시간 블럭처리
    def find_key(self,event):
        # self.entry.focus_set()
        txt.tag_remove("tmp_sel", "1.0", END)
        start="1.0"
        word=self.entry.get()
        length=len(word)
        if length>1:
            try:
                pos=txt.search(word, start, stopindex=END)
            except:
                pass
            else:
                while pos:
                    row, col = pos.split('.')
                    word_end = int(col) + length
                    word_end = row + '.' + str(word_end)
                    start=word_end
                    txt.tag_add("tmp_sel", pos, word_end)
                    pos=txt.search(word, start, stopindex=END)
        txt.tag_config("tmp_sel", background="skyblue", foreground="white")

    
    def find(self):
        txt.tag_remove("sel", "1.0", END)   # 기존 블록처리된거 없에기
        start=txt.index(INSERT)
        word=self.entry.get()
        pos = txt.search(word, start, stopindex=END)
        if not pos:
            start="1.0"
            pos = txt.search(word, start, stopindex=END)
            if not pos:
                msgbox.showerror("에러", f"{word}를 찾을 수 없습니다.")
                return
        length = len(word)
        row, col = pos.split('.')
        end = int(col) + length
        end = row + '.' + str(end)

        # 블럭처리 해줌(드래그된 상태)
        # 블럭처리 되면 커서도 블럭처리된 글자 앞으로이동
        # 현재 커서 위치 기준으로 다음 단어를 찾아주는 방식
        # insert마크를 가져와야 글자삽입 마크를 가져온다
        txt.tag_add("sel", pos, end)
        txt.mark_set(INSERT,SEL_LAST)
        root.update()
    
    def destroy_window(self): # 찾기 창 닫으면 태그 제거
        txt.tag_remove("tmp_sel", "1.0", END)
        self.UI.destroy()


    # 바꾸기
    # 찾기에 해당되는 단어를 찾아 드래그 해 준후 단어 바꾸고 나면 그다음 찾기 단어에 드래그
    def change(self):
        word=self.entry.get()
        changed_word=self.entry_change.get()
        try:
            txt.selection_get()
        except:
            self.find()
        else:
            x=txt.index(SEL_FIRST)
            y=txt.index(SEL_LAST)
            if word==txt.get(x,y):
                txt.delete(x,y)
                txt.insert(x,changed_word)
            self.find()

    # 모두바꾸기
    # 모두바꾸기는 드래그된 부분이 있으면 드래그된 부분 내에서만 바꾸도록 구현해봄

    def change_all(self):
        word=self.entry.get()
        changed_word=self.entry_change.get()
        try:
            txt.selection_get()
        # 블록처리 없으면 모두바꾸고
        except:
            start="1.0"
            end=txt.index(END)
        # 블록처리 있으면 해당부분만 바꿈
        else:
            start=txt.index(SEL_FIRST)
            end=txt.index(SEL_LAST)

        pos=txt.search(word, start, stopindex=end)
        if not pos:
                msgbox.showerror("에러", f"{word}를 찾을 수 없습니다.")
                return
        while pos:
            length=len(word)
            row, col = pos.split('.')
            word_end = int(col) + length
            word_end = row + '.' + str(word_end)
            txt.delete(pos, word_end)
            txt.insert(pos,changed_word)
            pos=txt.search(word, start, stopindex=end)



# 메뉴함수

# 파일메뉴 함수
# 오픈시 저장여부
def yesnocancel():
    response=msgbox.askyesnocancel(title="변경 저장", message=f"변경내용을 저장하시겠습니까?")
    return response
    # 예=1 아니오=0 취소=-1

# 변화 내용을 감지해서 저장할지 물어봄
def check_save():
        
    file_list = os.listdir(get_cur_path())
    if file_list.count(root.title()): # 현재 제목을 가진 파일이 있는지 확인
        f=open(os.path.join(get_cur_path(),root.title()), "r", encoding="UTF-8")
        data=f.read()
        f.close()
    else:
        data="\n"   # \n 으로 해야 공백 text박스와 일치
    # 현재 파일 내용이 원본과 다르면
    # 저장할지 여부 묻기
    if txt.get("1.0", END)!=data:
        res=yesnocancel()
        if res==1:  # 예: 저장
            f_save=open(os.path.join(get_cur_path(),root.title()), "w", encoding="UTF-8")
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
def open_file(event=None):
    if check_save() != -1:
        UI_open(root)

def save_file(event=None):
    # 새 창일경우 파일이름 설정
    if is_newtap:
        UI_save(root)

    else:
        f=open(os.path.join(get_cur_path(),root.title()), "w", encoding="UTF-8")
        data=txt.get("1.0", END)
        f.write(data)
        f.close
# 끝내기
def cmd_quit():
    if check_save() !=-1:
        root.quit()

# 새창
def new_tap(event=None):
    if check_save()==-1:
        return
    global is_newtap
    is_newtap=True
    root.title("제목 없음")
    txt.delete("1.0", END)

# 다른이름으로 저장
def save_as(event=None):
    UI=UI_save(root)

# 편집메뉴 함수
def find_word(event=None):
    UI=UI_find()

# 메뉴
menu=Menu(root)
menu_file=Menu(menu, tearoff=0)
menu_edit=Menu(menu, tearoff=0)
menu_text=Menu(menu, tearoff=0)
menu_view=Menu(menu, tearoff=0)
menu_help=Menu(menu, tearoff=0)
# 메뉴 파일
menu_file.add_command(label=f'{"새로만들기":<23}{"Ctrl+n":>12}', command=new_tap)
root.bind("<Control-n>",new_tap)
menu_file.add_separator()
menu_file.add_command(label=f'{"열기":<29}{"Ctrl+o":>12}', command=open_file)
root.bind("<Control-o>",open_file)
menu_file.add_command(label=f'{"저장":<29}{"Ctrl+s":>12}', command=save_file)
root.bind("<Control-s>",save_file)
menu_file.add_command(label=f'{"다른 이름으로 저장":<16}{"Ctrl+Shift+s":>12}', command=save_as)
root.bind("<Control-Shift-S>",save_as)  # shift 가 들어가서 대문자로 S해줘야하나?
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=cmd_quit)

menu.add_cascade(label="파일", menu=menu_file)
# 메뉴 편집
menu_edit.add_command(label="실행 취소".ljust(12)+"Ctrl+z".rjust(8), command=txt.edit_undo)
# root.bind("<Control-z>",txt.edit_undo)
menu_edit.add_command(label="다시 실행".ljust(12)+"Ctrl+y".rjust(8), command=txt.edit_redo)
# root.bind("<Control-y>",txt.edit_redo)
menu_edit.add_command(label="찾기/바꾸기".ljust(10)+"Ctrl+f".rjust(8), command=find_word)
root.bind("<Control-f>",find_word)

menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_text)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)






root.config(menu=menu)
root.mainloop()
