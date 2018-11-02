from tkinter import *
t=Text()
t.pack()

for i in range(1,31):
    t.insert(END, '%s\n' % i)

def f(event):
    if event.keysym == 'Return':
        t.mark_set('insert', 0.0)
        
while True:
    t.see(END)

t.bind('<KeyPress>', f)

t.mainloop()
