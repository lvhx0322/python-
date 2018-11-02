import tkinter as tk


window = tk.Tk()

window.title('TEST')
window.geometry('200x100')

var = tk.StringVar()

l = tk.Label(window, textvariable=var, bg='blue', font=('Arial', 13),
    width=15, height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('hiting!!!')
    else:
        on_hit = False
        var.set('no')

b = tk.Button(window, text='Hit Me!', bg='red', width=15, height=2, command=hit_me)
b.pack()

window.mainloop()

