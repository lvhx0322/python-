import tkinter as tk

window = tk.Tk()
window.title('TEST')
window.geometry('200x200')

e = tk.Entry(window, show='**')
e.pack()

def insert_point():
    e.clear()
    var = e.get()
    t.insert('insert', var)

def insert_end():
    var = e.get()
    t.insert('end', var)

def insert_position():
    var = e.get()
    t.insert(1.1, var)


b1 = tk.Button(window, text='insert point',  command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

b3 = tk.Button(window, text='insert 1.1', command=insert_position)
b3.pack()

t = tk.Text(window, height=2)
t.pack()

window.mainloop()
