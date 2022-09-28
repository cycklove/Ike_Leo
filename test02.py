import pymysql
from random import randint
from win32con import MB_OK, MB_ICONWARNING,MB_ICONINFORMATION

ip = '192.168.1.165'
zh = 'root'
mm = 'caokai3220251'
dbase = 'guanli'

cxsql = 'select name from cj_user where IS_ENABLE=1'

def name():
    db = pymysql.connect(host=ip, user=zh, password=mm, database=dbase)
    cursor = db.cursor()
    cursor.execute(cxsql)
    data = cursor.fetchone()
    f = open('name.txt', 'w')
    f.write('')
    f = open('name.txt', 'a')
    while data:
        f.write(str(data[0]))
        f.write('\n')
        data = cursor.fetchone()
    db.commit()
    cursor.close()
    db.close()
    f.close()
    # f.close()



wordlist3 = []
with open('name.txt') as f:
    for line in f.readlines():
        wordlist3.append(line.strip('\n'))  # strip('\n')去掉字符串中的'\n'
name_list = wordlist3

name = name_list[randint(0, len(name_list) - 1)]
print("恭喜{}！！！".format(name))
