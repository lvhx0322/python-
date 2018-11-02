from socket import *
import sys
import re

## 客户端登录部分
def do_login(s):
    while True:
        usrname = input('请输入用户名：')
        passwd = input('请输入密码：')
        l1 = re.findall(r'[^0-9A-Za-z]', usrname)
        l2 = re.findall(r'[^0-9A-Za-z]', passwd)
        if l1 == [] and l2 == []:
            msg = '#lgin#%s$%s' % (usrname, passwd)
            s.send(msg.encode())
        else:
            print('输入的用户名和密码不符合格式，请重新输入！')
            continue
        data = s.recv(1024).decode()
        if data == '#OK#':
            print('登录成功！')
            return usrname
        elif data == '#UR#':
            print('登录失败，用户名不存在！')
            return 0
        elif data == '#PW#':
            print('登录失败，密码错误！')
            return 0
        else:
            print('登录失败，未知错误！')
            return 0

# 客户端注册部分
def do_register(s):
    while True:
        usrname = input('请输入用户名：')
        passwd = input('请输入密码：')
        passwd_re = input('请再次输入密码：')
        l1 = re.findall(r'[^0-9A-Za-z]', usrname)
        l2 = re.findall(r'[^0-9A-Za-z]', passwd)
        if l1 == [] and l2 == []:
            msg = '#rgst#%s$%s' % (usrname, passwd)
            if passwd != passwd_re:
                print('两次输入的密码不一致，请重新输入！')
                continue
            s.send(msg.encode())
        else:
            print('输入的用户名和密码不符合格式，请重新输入！')
            continue
        data = s.recv(1024).decode()
        if data == '#OK#':
            print('注册成功！')
            return
        elif data == '#UR#':
            print('用户名重复，请重试！')
        else:
            print('注册失败，请重试！')

#菜单１
def do_menu1(s):
    login_menu = '''
    ****************************
    1.登录    2.注册    3.退出
    ****************************
    '''
    while True:
        print(login_menu)
        order = input('>>>')
        if order == '1':
            usrname = do_login(s)
            if usrname:
                return usrname
            else:
                return 0
        elif order == '2':
            do_register(s)
        elif order == '3':
            s.send(b'#quit#')
            sys.exit(0)
        else:
            print('输入有误！')

#客户端对话部分
def do_conversation(s, usrname):
    while True:
        message = input('%s:' % usrname)
        if not message:
            break
        s.send(b'#conv#' + message.encode())
        data = s.recv(1024).decode()
        print(data)

#菜单２
def do_menu2(s, usrname):
    conversation_menu = '''
    ***************************
    1.对话   2.返回主菜单
    ***************************
    '''
    while True:
        print(conversation_menu)
        order = input('>>>')
        if order == '1':
            do_conversation(s, usrname)
        elif order == '2':
            return
        else:
            print('输入有误！')


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

    while True:
        usrname = do_menu1(s)
        if usrname:
            do_menu2(s, usrname)


if __name__ == '__main__':
    main()
