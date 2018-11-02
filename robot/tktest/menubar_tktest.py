import tkinter as tk


window = tk.Tk()
window.title = 'TEST'
window.geometry('200x200')

l = tk.Label(window, text='', bg='pink')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='you do %s' % counter)
    counter += 1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='submenu1', command=do_job)

window.config(menu=menubar)
window.mainloop()
