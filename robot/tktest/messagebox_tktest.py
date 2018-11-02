import tkinter as tk
from tkinter import messagebox


window = tk.Tk()
window.title = 'TEST'
window.geometry('200x200')

def hit_me():
    # messagebox.showinfo(title='Hi', message='hahaha')
    messagebox.showwarning(title='Hi', message='nonono')
    # messagebox.showerror(title='Hi', message='NO!!!!')
    # print(messagebox.askquestion(title='Hi', message='hahaha'))  # return 'yes' or 'no'
    # print(messagebox.askyesno(title='Hi', message='hahaha'))  # return True or False
    # print(messagebox.asktrycancel(title='Hi', message='hahaha'))  # return True or False  #????
    # print(messagebox.askokcancel(title='Hi', message='hahaha'))  # return True or False


tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()
