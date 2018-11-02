import tkinter as tk


window = tk.Tk()
window.title('TEST')
window.geometry('200x200')

l = tk.Label(window, bg='pink', width=20, text='empty')
l.pack()

def print_selection():
    if var1.get() and var2.get():
        l.config(text='I love both!')
    elif var1.get() and not var2.get():
        l.config(text='I love Python!')
    elif not var1.get() and var2.get():
        l.config(text='I love C!')
    else:
        l.config(text='I hate both!')



var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Python', 
    variable = var1, onvalue=1, offvalue=0, command=print_selection)
c2 = tk.Checkbutton(window, text='C', 
    variable = var2, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2.pack()

window.mainloop()
