import tkinter as tk

window = tk.Tk()
window.title('TEST')
window.geometry('200x200')


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


var1 = tk.StringVar()
l = tk.Label(window, bg='red', width=10, height=2, textvariable=var1)
l.pack()


b = tk.Button(window, text='print selection', width=15, height=2,
    command = print_selection)
b.pack()

var2 = tk.StringVar()
print(var2)
L = ['wr', 'Lucy', 'John']
var2.set(L) # 元组列表都行
print(var2)
lb = tk.Listbox(window, listvariable=var2)
list_items = [1,2,3,4]
for i in list_items:
    lb.insert('end', i)
lb.insert(1,'first')  # 索引插入
lb.insert(2,'second')  # 索引插入
lb.delete(2)   # 索引删除
lb.pack()

window.mainloop()
