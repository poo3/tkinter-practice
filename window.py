import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title("めもっちょう")
root.iconbitmap("notepad_icon.ico")
root.geometry('500x400')
root.config(bg='blue')

# サブウィンドウの作成
sub_window = tkinter.Toplevel()
sub_window.title('サブウィンドウDETH YO!')
sub_window.iconbitmap('notepad_icon.ico')
sub_window.geometry('300x300+500+500')
sub_window.config(bg='red')


# ウィンドウのループ処理
root.mainloop()
