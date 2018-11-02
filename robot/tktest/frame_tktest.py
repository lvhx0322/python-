import tkinter as tk


window = tk.Tk()
window.title = 'TEST'
window.geometry('200x200')

tk.Label(window, text='on the window', bg='pink').pack()

frm = tk.Frame(window)
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

tk.Label(frm_l, text='on the frm_l1', bg='pink').pack()
tk.Label(frm_l, text='on the frm_l2', bg='pink').pack()
tk.Label(frm_r, text='on the frm_r', bg='pink').pack()

window.mainloop()
