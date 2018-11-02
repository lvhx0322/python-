import tkinter as tk

window = tk.Tk()
window.title('登录窗口')
window.geometry('600x650')

# welcome image
canvas = tk.Canvas(window, height=300, width=600)
image_file = tk.PhotoImage(file='./hy.png')
image = canvas.create_image(0,0,anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name:', font=('Arial', 15)).place(x=125, y=300)
tk.Label(window, text='Password:', font=('Arial', 15)).place(x=125, y=350)

var_usr_name = tk.StringVar()
var_usr_passwd = tk.StringVar()
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=275, y=300)
entry_usr_passwd = tk.Entry(window, textvariable=var_usr_passwd)
entry_usr_passwd.place(x=275, y=350)

# login and sign up button
def usr_login():
    pass
    # usr_name = var_usr_name.get()
    # usr_passwdd = var_usr_passwdd.get()

def usr_sign_up():
    window.destroy() 
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('Sign up')
    window_sign_up.geometry('350x200')

btn_login = tk.Button(window, height=2, width=10, text='Login', command=usr_login)
btn_login.place(x=175, y=450)
btn_sign_up = tk.Button(window, height=2, width=10, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=350, y=450)

window.mainloop()
