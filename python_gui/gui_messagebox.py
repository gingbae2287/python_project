import tkinter.messagebox as msgbox
from tkinter import *
# messagebox는 팝업메세지에 사용
root=Tk()
root.title("GUI")
root.geometry("480x480+400+100")
root.resizable(False, False)

def info():
    msgbox.showinfo("알림", "정상예매 완료")    # 첫번째 인자: 박스 제목, 두번쨰: 내용

def warning():
    msgbox.showwarning("경고", "해당좌석 매진.")

def error():
    msgbox.showerror("에러", "결제오류발생")

def okcancel():
    msgbox.askokcancel("예매??", "해당 좌석 유아동반석, 예매?")

def retrycancel():
    res=msgbox.askretrycancel("재시도 알림", "일시적오류. 다시시도?")
    print(res)
    if res==1:
        print("재시도")
    elif res==0:
        print("취소")

def yesno():
    msgbox.askyesno("골라골라", "해당좌석 역방향. 예매??")

def yesnocancel():
    response=msgbox.askyesnocancel(title=None, message="아아라라라")
    #print(response) # True False None
    if response==1:
        print("예")
    elif response==0:
        print("아니오")
    else:
        print("취소")
        root.quit()

def quit():
    root.quit()
Button(root, command=info, text="알림").pack()
Button(root, command=warning, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()
Button(root, command=quit, text="종료").pack()
root.mainloop()