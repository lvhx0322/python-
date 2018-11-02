from socket import *
import sys
import select
import re
import pymysql
import random
import os
from pymysql.err import InternalError

# 服务器登录部分
def do_login(conn, data, cursor):
    l = data.split('$')
    usrname = l[0]
    passwd = l[1]
    sql = "select passwd from users where name='%s'" % usrname
    cursor.execute(sql)
    tmp = cursor.fetchone()
    ret = ()
    if tmp:
        ret = tmp
    if ret == ():
        conn.send(b'#UR#')
    else:
        if passwd in ret:
            conn.send(b'#OK#')
        else:
            conn.send(b'#PW#')

# 服务器注册部分
def do_register(conn, data, db, cursor):
    l = data.split('$')
    usrname = l[0]
    passwd = l[1]
    sql = "select passwd from users where name='%s'" % usrname
    cursor.execute(sql)
    ret = cursor.fetchone()
    if ret is None:
        try:
            sql = "insert into users values(NULL, '%s', '%s')" % (
                usrname, passwd)
            cursor.execute(sql)
            db.commit()
            print('新注册用户：%s' % usrname)
            conn.send(b'#OK#')
        except Exception as e:
            db.rollback()
            conn.send(b'#ER#')
            raise e
    else:
        conn.send(b'#UR#')

#服务器对话部分
def do_conversation(conn, data, txtlist):
    for i in txtlist:
        # 取出文本中第一行，并将词汇分开
        sen = re.match(r'(^.+)\n', i).group(1)
        rwords = sen.split('|')
        for rw in rwords:
            match_wrds = re.findall(rw, data, re.I)
            # 检测是否能匹配到data里的词汇
            if match_wrds:
                ans_list = re.findall(r'\n  :(.+)', i)
                mesg = random.choice(ans_list)
                conn.send(mesg.encode())
                return  # 只发送一条回应
    else:
        conn.send('听不懂！听不懂！听不懂！'.encode())



def getConvData(db, cursor, filepath, fields='txtcontent'):
    try:
        sql = "select {} from convs into outfile '{}';".format(fields,filepath)
        cursor.execute(sql)
        print('获取数据库成功!')
        sys.exit(0)
    except Exception as e:
        print('获取数据库失败, error at', e)
        sys.exit(1)



def saveConvData(db, cursor, filepath):
    try:
        sql = "load data infile '{}' into table convs(txtcontent);".format(filepath)
        cursor.execute(sql)
        db.commit()
        print('保存到数据库成功!')
        sys.exit(0)
    except Exception as e:
        print('保存到数据库失败, error at', e)
        sys.exit(1)



def init_mysql():
    ##mysql　initialization##
    try:
        db = pymysql.connect('localhost', 'root', '123456',
                             'robot', charset='utf8')
        cursor = db.cursor()
    except InternalError as e:
        print(e)
        while True:
            order = input('数据库robot尚未创建，是否自动创建？(y/n)')
            if order == 'y':
                db = pymysql.connect('localhost', 'root', '123456', charset='utf8')
                cursor = db.cursor()
                sql = 'create database robot default charset=utf8;'
                cursor.execute(sql)
                cursor.execute('use robot;')
                sql = 'create table users(_id int primary key auto_increment, \
                                          name varchar(64) unique, \
                                          passwd varchar(64));'
                cursor.execute(sql)
                sql = 'create table convs(txtcontent LONGTEXT);'
                cursor.execute(sql)
                print('创建数据库成功！')
                break
            elif order == 'n':
                print('请自行创建数据库！')
                sys.exit(0)
            else:
                print('输入错误！')
    return (db, cursor)

def init_txt():
    ##txt　initialization##
    FILE = './conversation.txt'
    with open(FILE, 'rb') as f:
        ALLTXT = ''
        for line in f:
            ALLTXT += line.decode()
    L = re.split(r'.\n\n', ALLTXT)
    return L


def main():
    if len(sys.argv) == 3:
        HOST = sys.argv[1]
        POST = int(sys.argv[2])
        ADDR = (HOST, POST)
        db, cursor = init_mysql()
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'savedata':
            db, cursor = init_mysql()
            # path = os.getcwd()+ '/conversation.txt'
            path = '/var/lib/mysql-files/conversation.txt'
            saveConvData(db, cursor, path)
        elif sys.argv[1] == 'getdata':
            db, cursor = init_mysql()
            # path = os.getcwd()+ '/conversation.txt'
            path = '/var/lib/mysql-files/conversation.txt'
            getConvData(db, cursor, path)
        else:
            print('argv error!')
            sys.exit(1)
    else:
        print('argv error!')
        sys.exit(1)


    L = init_txt()


    ##socket　initialization##
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    rlist, wlist, xlist = [s], [], [s]
    while True:
        rl, wl, xl = select.select(rlist, wlist, xlist)
        for r in rl:
            if r == s:
                conn, addr = r.accept()
                print('connect from', addr)
                rlist.append(conn)
                xlist.append(conn)
            else:
                data = r.recv(1024).decode()
                if data[:6] == '#lgin#':
                    do_login(r, data[6:], cursor)
                elif data[:6] == '#rgst#':
                    do_register(r, data[6:], db, cursor)
                elif data[:6] == '#quit#':
                    rlist.remove(r)
                    xlist.remove(r)
                    print(r, 'quit!')
                elif data[:6] == '#conv#':
                    do_conversation(r, data[6:], L)

        for x in xl:
            if x == s:
                print('服务器异常！')
                sys.exit(2)
            else:
                print('链接异常！')


if __name__ == '__main__':
    main()
