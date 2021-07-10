# UI_file.py
# 파일 열기, 저장 기본 틀
import tkinter.messagebox as msgbox
from tkinter import *
import os


####################
current_path=os.path.dirname(__file__)
prev_path=os.path.split(current_path)[0]
dir_list=current_path.split("\\")

#########

class UI_file:
    def __init__(self,root):
        self.root=root
        self.UI=Toplevel(self.root)
        self.UI.title("열기")
        self.UI.geometry("480x300")
        self.UI.resizable(True, True)
        # 프레임
        self.current_folder_name="folder: "+os.path.split(current_path)[1]

        self.frame_path=Frame(self.UI, relief="solid", bd=1)
        self.frame_folder=LabelFrame(self.UI,text=self.current_folder_name, relief="solid",bd=1)
        self.frame_file=LabelFrame(self.UI,text="files", relief="solid",bd=1)
        self.frame_bottom=Frame(self.UI, relief="solid",bd=1, height=5)
        self.frame_path.grid(row=0,column=0,columnspan=2,sticky=N+E+W+S,padx=3,pady=3)
        self.frame_folder.grid(row=1,column=0, rowspan=2,sticky=N+E+W+S,padx=3,pady=3)
        self.frame_file.grid(row=1,column=1,rowspan=2,sticky=N+E+W+S,padx=3,pady=3)
        self.frame_bottom.grid(row=3,column=0, columnspan=2,sticky=N+E+W+S,padx=3,pady=3)
        

        # 리스트 박스
        # 스크롤바
        self.scroll1=Scrollbar(self.frame_folder)
        self.scroll2=Scrollbar(self.frame_file)
        self.scroll1.pack(side="right", fill="y")
        self.scroll2.pack(side="right", fill="y")
        # 폴더와 파일 리스트
        self.file_list = os.listdir(current_path)  
        # 폴더랑 파일 구분해서 보여줘야함
        self.list_folders=Listbox(self.frame_folder, selectmode="single",width=30, height=10,yscrollcommand = self.scroll1.set)
        self.list_files=Listbox(self.frame_file, selectmode="single",width=30, height=10,yscrollcommand = self.scroll2.set)
        for file_name in self.file_list:
            if os.path.isdir(os.path.join(current_path,file_name)):
                self.list_folders.insert(END, file_name)
            else:
                self.list_files.insert(END, file_name)
        self.list_folders.pack(side="left")
        self.list_files.pack(side="left")

        self.scroll1["command"]=self.list_folders.yview
        self.scroll2["command"]=self.list_files.yview
       
        # 파일리스트 선택시 동작 bind
        self.list_files.bind("<<ListboxSelect>>", self.get_file_name)
        
        # 폴더리스트 bind
        self.list_folders.bind("<<ListboxSelect>>", self.delete_file_name)
        self.list_folders.bind("<Double-Button-1>", self.open_folder_by_click)
        
        # 하단 파일 이름 및 버튼
        self.file_name_txt=Entry(self.frame_bottom, width=50)
        self.btn_cancel=Button(self.frame_bottom, text="취소", command=self.UI.destroy)
        self.file_name_txt.grid(row=0,column=0)
        self.btn_cancel.grid(row=0,column=2)
        
        # directory
        # 버튼두개는 현재, 바로전 디렉토리 폴더 이름.
        # StringVar를 이용해 자동으로 바뀌도록 해야함
        self.dir1=StringVar()
        self.dir2=StringVar()
        self.dir1.set(dir_list[len(dir_list)-1])
        self.dir2.set(dir_list[len(dir_list)-2])
        self.label_path=Label(self.frame_path,text="Path: ")
        self.btn_dir1=Button(self.frame_path, textvariable=self.dir1, padx=3,pady=3)
        self.btn_dir2=Button(self.frame_path, textvariable=self.dir2, padx=3,pady=3, command=self.prev_dir)
        self.btn_folder_list=Menubutton(self.frame_path, text=">>", padx=3, pady=3,relief="solid",bd=1)
        self.menu_prev_folders=Menu(self.btn_folder_list, tearoff=0)
        self.idx_folder=IntVar()
        self.menu_prev_folders.bind('<<MenuSelect>>', self.test_bind)

        self.label_path.grid(row=0, column=0,sticky=N+E+W+S)
        self.btn_dir2.grid(row=0, column=1,sticky=N+E+W+S)
        self.btn_folder_list.grid(row=0, column=2,sticky=N+E+W+S)
        self.btn_dir1.grid(row=0, column=3,sticky=N+E+W+S)
        
        # >>버튼에 나올 폴더리스트 변경
        self.chg_dir()
        
        self.btn_folder_list["menu"]=self.menu_prev_folders
        
        # 상속받는 클래스에서 mainloop 써줘야함. 여기서 쓰면 상속 받는 클래스의 init이 실행 안댐
        # self.UI.mainloop()

    def test_bind(self,event):
        # 코드가져옴 call함수 아직 이해 불가
        check = self.root.call(event.widget, "index","active")
        if check != "none":
            self.idx_folder.set(check)
            #chg_dir 에서 바뀐 prev_folder_list 에 index로 접근
            #self.go_dir(self.prev_folder_list[self.idx_folder])

    def update_dir(self):
        global prev_path
        prev_path=os.path.split(current_path)[0]
        dir_list=current_path.split("\\")
        self.file_name_txt.delete(0, END)
        self.dir1.set(dir_list[len(dir_list)-1])
        self.dir2.set(dir_list[len(dir_list)-2])
        self.file_list = os.listdir(current_path)
        # 리스트박스도 수정해줌
        self.list_files.delete(0,END)
        self.list_folders.delete(0,END)
        for file_name in self.file_list:
            if os.path.isdir(os.path.join(current_path,file_name)):
                self.list_folders.insert(END, file_name)
            else:
                self.list_files.insert(END, file_name)
        ####디렉토리 이동 공통####
        self.chg_dir()
        self.current_folder_name="folder: "+os.path.split(current_path)[1]
        self.frame_folder.configure(text=self.current_folder_name)

    def prev_dir(self):
        # 디렉토리 변경을위해 경로에서 디렉토리 하나를 뺴줌
        self.file_name_txt.delete(0, END)
        global current_path
        dir_list.pop()
        current_path=prev_path
        self.update_dir()
        
    def chg_dir(self):
        # 리스트내포써봄 바로 전 디렉토리내의 디렉토리 리스트중 폴더인 것들만 리스트에 포함
        self.prev_folder_list= [i for i in os.listdir(prev_path) if os.path.isdir(os.path.join(prev_path,i))]
        self.menu_prev_folders.delete(0,END)
        # 바인드로 해봐야게씀
        # 바인드menuselet>> 메뉴항목에 커서 올라가면 작동
        # 메뉴항목 인덱스를 값으로 저장.
        # go_dir 실행시 인덱스 가져와서 폴더명 가져옴
        for folder in self.prev_folder_list:
            self.menu_prev_folders.add_command(label=folder, command=self.menu_bind) #command=lambda: self.go_dir(self.folder_list.entrycget(0,'label')))
        

    def menu_bind(self):
        # 이전 폴더의 폴더리스트중 고르면 경로 합쳐서 이동
        tmp_path=os.path.join(prev_path,self.prev_folder_list[self.idx_folder.get()])
        self.go_path(tmp_path)

    def go_path(self, path):
        global current_path
        global dir_list
        current_path=path
        self.update_dir()


    def open_folder(self):
        #global is_newtap
        global current_path
        # file_name=self.file_name_txt.get()
        # if not file_name:
        #     msgbox.showerror("error", "폴더 또는 파일명을 입력하세요.")
        #     return
        # 파일인지 폴더인지 판단
        # if os.path.isdir(os.path.join(current_path,file_name)): # 폴더
        #     self.file_name_txt.delete(0, END)
        #     current_path=os.path.join(current_path, file_name)
        #     dir_list.append(file_name)
        #     self.update_dir()
        # else:
        #     try:
        #         f=open(os.path.join(current_path,file_name), "r", encoding="UTF-8")
        #     except:
        #         msgbox.showerror("error", "존재하지 않는 파일입니다.")
        #     else:
        #         data=f.read()[:-1]  # 마지막에 \n가 기입돼서 지워줌
        #         # 메인 ui에서 동작하게 해야함
        #         is_newtap=False
        #         txt.delete("1.0", END)
        #         txt.insert("1.0",data)
        #         root.title(file_name)
        #         self.UI.destroy()
        #         cancel(self)

    def get_file_name(self, event):
        widget = event.widget   # 현재 이벤트의 위젯정보 (listbox)
        try:
            file_name=widget.get(widget.curselection())
        except:
            pass
        else:
            self.file_name_txt.delete(0, END)
            self.file_name_txt.insert(0,file_name)
    
    def delete_file_name(self,event):
        widget = event.widget
        try:
            widget.get(widget.curselection())
        except:
            pass
        else:
            self.file_name_txt.delete(0, END)

    def open_folder_by_click(self,event):
        widget=event.widget
        try:
            # if widget.curselection():
            folder_name=widget.get(widget.curselection())
        except:
            pass
        else:
            self.go_path(os.path.join(current_path,folder_name))

def get_cur_path():
    return current_path