import tkinter as tk
import time


def return_main1():
    pass


usrname = 'wr'
def sendMsgEvent(event):
    if event.keysym == 'Return':
        send_message()

        
def send_message():
    mesg = usrname+' :' + time.strftime("%Y-%m-%d %H:%M:%S",  
                                  time.localtime()) + '\n'
    msg_show.insert(tk.END, mesg, 'greencolor')
    msg_show.insert(tk.END, msg_send.get(0.0, tk.END))
    msg_send.delete(0.0, tk.END)

window_conv = tk.Tk()
window_conv.title('自动回复机器人')

f_msgshow = tk.Frame(width=500, height=300)
f_msgsend = tk.Frame(width=500, height=200)
f_msgbutton = tk.Frame(width=500, height=30)
f_msgsidebar = tk.Frame(width=250, height=560)

f_msgshow.grid(row=0, column=0, padx=5, pady=2)
f_msgsend.grid(row=1, column=0, padx=5, pady=2)
f_msgbutton.grid(row=2, column=0)
f_msgsidebar.grid(row=0, column=1, rowspan=4, pady=2)

msg_show = tk.Text(f_msgshow)
msg_show.grid(row=0, column=0)
msg_send = tk.Text(f_msgsend)
msg_send.grid(row=1, column=0)
msg_button1 = tk.Button(f_msgbutton, text='Send', width=8, command=send_message)
msg_button1.grid(row=2, column=0, padx=2, sticky=tk.W)
msg_button2 = tk.Button(f_msgbutton, text='Cancel', width=8)
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

