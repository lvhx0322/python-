from socket import *
import sys
import re
import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import time


def do_login(window_log, s, usrname, passwd):
    l1 = re.findall(r'[^0-9A-Za-z]', usrname)
    l2 = re.findall(r'[^0-9A-Za-z]', passwd)
    if l1 == [] and l2 == []:
        msg = '#lgin#%s$%s' % (usrname, passwd)
        s.send(msg.encode())
    else:
        messagebox.showerror(title='登录失败',
                             message='输入的用户名和密码不符合格式，请重新输入！')
        return 0
    data = s.recv(1024).decode()
    if data == '#OK#':
        mesg = '登录成功！欢迎你 %s ！' % usrname
        messagebox.showinfo(title='登录成功',
                            message=mesg)
        window_log.destroy()
        do_menu2(s, usrname)
    elif data == '#UR#':
        messagebox.showerror(title='登录失败',
                             message='登录失败，用户名不存在！')
        return 0
    elif data == '#PW#':
        messagebox.showerror(title='登录失败',
                             message='登录失败，密码错误！')
        return 0
    else:
        messagebox.showerror(title='登录失败',
                             message='登录失败，未知错误！')
        return 0


def do_register(window_log, s):
    window_rgst = tk.Toplevel(window_log)
    window_rgst.title('注册新用户')
    window_rgst.geometry('500x500')

    # user information
    tk.Label(window_rgst, text='User name:',
             font=('Arial', 15)).place(x=125, y=200)
    tk.Label(window_rgst, text='Password:',
             font=('Arial', 15)).place(x=135, y=250)
    tk.Label(window_rgst, text='Password confirm:',
             font=('Arial', 15)).place(x=75, y=300)

    var_usr_name = tk.StringVar()
    var_usr_passwd = tk.StringVar()
    var_usr_passwdcf = tk.StringVar()
    entry_usr_name = tk.Entry(window_rgst, textvariable=var_usr_name)
    entry_usr_name.place(x=275, y=200)
    entry_usr_passwd = tk.Entry(
        window_rgst, textvariable=var_usr_passwd, show='*')
    entry_usr_passwd.place(x=275, y=250)
    entry_usr_passwdcf = tk.Entry(
        window_rgst, textvariable=var_usr_passwdcf, show='*')
    entry_usr_passwdcf.place(x=275, y=300)

    # login and sign up button
    btn_register = tk.Button(window_rgst, height=2, width=10, text='注册',
                             command=lambda: check_register(window_rgst, s, var_usr_name.get(), 
                             var_usr_passwd.get(), var_usr_passwdcf.get()))

    btn_register.place(x=220, y=350)


def check_register(window_rgst, s, usrname, passwd, passwdcf):
    l1 = re.findall(r'[^0-9A-Za-z]', usrname)
    l2 = re.findall(r'[^0-9A-Za-z]', passwd)
    if passwd != passwdcf:
        messagebox.showerror(title='注册失败',
                             message='两次输入的密码不一致，请重新输入！')
        return 0
    if l1 == [] and l2 == []:
        msg = '#rgst#%s$%s' % (usrname, passwd)
        s.send(msg.encode())
    else:
        messagebox.showerror(title='注册失败',
                             message='输入的用户名和密码不符合格式，请重新输入！')
        return 0
    data = s.recv(1024).decode()
    if data == '#OK#':
        messagebox.showinfo(title='注册成功',
                            message='注册成功！')
        window_rgst.destroy()
        return 1
    elif data == '#UR#':
        messagebox.showerror(title='注册失败',
                             message='用户名重复，请重试！')
    else:
        messagebox.showerror(title='注册失败',
                             message='注册失败，请重试！')


def do_menu1(s):
    window_log = tk.Tk()
    window_log.title('自动回复机器人')
    window_log.geometry('600x650')

    # welcome image
    canvas = tk.Canvas(window_log, height=300, width=600)
    image_file = tk.PhotoImage(file='./hy.png')
    image = canvas.create_image(0, 0, anchor='nw', image=image_file)
    canvas.pack(side='top')

    # user information
    tk.Label(window_log, text='User name:',
             font=('Arial', 15)).place(x=125, y=300)
    tk.Label(window_log, text='Password:', font=(
        'Arial', 15)).place(x=125, y=350)

    var_usr_name = tk.StringVar()
    var_usr_passwd = tk.StringVar()
    entry_usr_name = tk.Entry(window_log, textvariable=var_usr_name)
    entry_usr_name.place(x=275, y=300)
    entry_usr_passwd = tk.Entry(
        window_log, textvariable=var_usr_passwd, show='*')
    entry_usr_passwd.place(x=275, y=350)

    # login and sign up button
    btn_login = tk.Button(window_log, height=2, width=10, text='登录',
                          command=lambda: do_login(window_log, s, var_usr_name.get(), var_usr_passwd.get()))
    btn_login.place(x=175, y=450)
    btn_register = tk.Button(window_log, height=2, width=10, text='注册',
                             command=lambda: do_register(window_log, s))
    btn_register.place(x=350, y=450)

    window_log.mainloop()


def do_menu2(s, usrname):

    def return_menu1(window_conv, s):
        if messagebox.askokcancel(title='返回主菜单', message='确定退出登录，并返回主菜单吗？'):
            window_conv.destroy()
            do_menu1(s)

    def sendMsgEvent(event):
        if event.keysym == 'Return':
            send_message()

    def send_message():
        usr_send = msg_send.get(0.0, tk.END) + '\n'
        mesg1 = usrname+'   ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                              time.localtime()) + '\n'
        msg_show.insert(tk.END, mesg1, 'greencolor')
        msg_show.insert(tk.END, usr_send)
        msg_send.delete(0.0, tk.END)

        s.send(b'#conv#' + usr_send.encode())
        data = s.recv(1024).decode() + '\n'
        mesg2 = 'robot   ' + time.strftime("%Y-%m-%d %H:%M:%S",
                                           time.localtime()) + '\n'
        msg_show.insert(tk.END, mesg2, 'greencolor')
        msg_show.insert(tk.END, data)
        msg_show.see(tk.END)
        msg_send.mark_set('insert', 0.0)

    window_conv = tk.Tk()
    window_conv.title('自动回复机器人')

    f_msgshow = tk.Frame(width=510, height=300)
    f_msgsend = tk.Frame(width=510, height=200)
    f_msgbutton = tk.Frame(width=510, height=30)
    f_msgsidebar = tk.Frame(width=300, height=560)

    f_msgshow.grid(row=0, column=0, padx=5, pady=2)
    f_msgsend.grid(row=1, column=0, padx=5, pady=2)
    f_msgbutton.grid(row=2, column=0)
    f_msgsidebar.grid(row=0, column=1, rowspan=4, pady=2)

    msg_show = ScrolledText(f_msgshow, width=70, height=20)
    msg_show.grid(row=0, column=0)
    msg_send = ScrolledText(f_msgsend, width=70, height=14)
    msg_send.grid(row=1, column=0)
    # 按钮
    msg_button1 = tk.Button(f_msgbutton, text='Send',
                            width=8, command=send_message)
    msg_button1.grid(row=2, column=0, padx=2, sticky=tk.W)
    msg_button2 = tk.Button(f_msgbutton, text='Cancel',
                            width=8, command=lambda: return_menu1(window_conv, s))
    msg_button2.grid(row=2, column=1, padx=2)
    # 插入图片
    img = tk.PhotoImage(file='./robot2.png')
    msg_pic = tk.Label(f_msgsidebar, image=img)
    msg_pic.imge = img
    msg_pic.grid(row=0, column=1, rowspan=3)

    msg_send.bind('<KeyPress-Return>', sendMsgEvent)

    f_msgshow.grid_propagate(0)
    f_msgsend.grid_propagate(0)
    f_msgbutton.grid_propagate(0)
    f_msgsidebar.grid_propagate(0)

    window_conv.mainloop()


def main():
    if len(sys.argv) == 3:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        ADDR = (HOST, PORT)
    else:
        print('argv error')
        sys.exit(1)

    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.connect(ADDR)

    do_menu1(s)


if __name__ == '__main__':
    main()
