import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Create Button')
root.iconbitmap('notepad_icon.ico')
root.geometry('500x500')
root.resizable(0, 0)
root.config(bg='red')

# ボタンの作成
button_1 = tkinter.Button(root, text='ボタン')
button_1.grid(row=0, column=0)

button_2 = tkinter.Button(root, text='button2')
button_2.grid(row=0, column=1,)

button_3 = tkinter.Button(root, text='button3',
                          bg='pink', activebackground='yellow')
button_3.grid(row=0, column=2, padx=10, pady=10, ipadx=5, ipady=5)

button_4 = tkinter.Button(root, text='button4', borderwidth=5)
button_4.grid(row=1, column=0, columnspan=3, sticky='WE')

# ウィンドウのループ処理
root.mainloop()
