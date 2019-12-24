import pymssql #引入pymssql模块
import time
import traceback

def ywxtselect():

    ywipall = ['192.168.101.16','192.168.101.21','192.168.101.26','192.168.101.29','192.168.101.32','192.168.101.35','192.168.101.53','192.168.101.38','192.168.101.44','192.168.101.41','192.168.101.47','192.168.101.50','192.168.101.56','192.168.101.59','192.168.101.62','192.168.101.65','192.168.101.68','192.168.101.71','192.168.101.74','192.168.101.77','192.168.101.80','192.168.101.83','192.168.101.86','192.168.101.93','192.168.101.95','192.168.101.57','192.168.101.58']

    for i in ywipall:
        connect = pymssql.connect(i, 'sa', 'AAAaaa123', 'cyls1')  # 建立连接

        cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
        sql = "select id,CONVERT(nvarchar(100),mc) from tb_gsjg where id = dbo.f_get_gsjg()"
        cursor.execute(sql)  # 执行sql语句
        row = cursor.fetchone()  # 读取查询结果,
        while row:  # 循环读取所有结果
            print("机构ID=%s,机构名称=%s" %(row[0],row[1]),"系统IP=",i) # 输出结果
            row = cursor.fetchone()
            time.sleep(0.2)

        # connect.commit()  # 提交 查询语句时不需要此条
        cursor.close()
        connect.close()



def ywxtproc():
    ywipall = ['192.168.101.16', '192.168.101.21', '192.168.101.26', '192.168.101.29', '192.168.101.32',
               '192.168.101.35', '192.168.101.53', '192.168.101.38', '192.168.101.44', '192.168.101.41',
               '192.168.101.47', '192.168.101.50', '192.168.101.56', '192.168.101.59', '192.168.101.62',
               '192.168.101.65', '192.168.101.68', '192.168.101.71', '192.168.101.74', '192.168.101.77',
               '192.168.101.80', '192.168.101.83', '192.168.101.86', '192.168.101.93', '192.168.101.95',
               '192.168.101.57', '192.168.101.58']

    for i in ywipall:
        connect = pymssql.connect(i, 'sa', 'AAAaaa123', 'cyls1')  # 建立连接

        cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
        # sql1 = f"exec sp_dropserver @server='smb',@droplogins='droplogins'"
        # sql2 = "exec sp_addlinkedserver 'smb','','SQLOLEDB','192.168.101.111'"
        # sql3 = "exec sp_addlinkedsrvlogin 'smb','false',null,'sa','AAAaaa123'"
        # print(i,"OK")
        cursor.execute("exec p_cb_ike_gsjg ")  # 执行proc 不支持带事务的proc
        result = cursor.fetchall()  # 得到结果集
        for ii in result:
            print(ii)  # 遍历打印查询结果集的数据
        connect.commit()  # 提交 查询语句时不需要此条
        cursor.close()
        connect.close()

def ywxtupdeins():

        ywipall = ['192.168.101.16', '192.168.101.21', '192.168.101.26', '192.168.101.29', '192.168.101.32',
               '192.168.101.35', '192.168.101.53', '192.168.101.38', '192.168.101.44', '192.168.101.41',
               '192.168.101.47', '192.168.101.50', '192.168.101.56', '192.168.101.59', '192.168.101.62',
               '192.168.101.65', '192.168.101.68', '192.168.101.71', '192.168.101.74', '192.168.101.77',
               '192.168.101.80', '192.168.101.83', '192.168.101.86', '192.168.101.93', '192.168.101.95',
               '192.168.101.57', '192.168.101.58']

        for i in ywipall:
            connect = pymssql.connect(i, 'sa', 'AAAaaa123', 'cyls1')  # 建立连接


            cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
        # sql1 = f"exec sp_dropserver @server='smb',@droplogins='droplogins'"
        # sql2 = "exec sp_addlinkedserver 'smb','','SQLOLEDB','192.168.101.111'"
        # sql3 = "exec sp_addlinkedsrvlogin 'smb','false',null,'sa','AAAaaa123'"
        # print(i,"OK")
            cursor.execute("insert into cb_link(bm,mc,ip) select 'smthk','商贸退货库','192.168.101.92'")  # 执行sql
            connect.commit()  # 提交 查询语句时不需要此条
            cursor.close()
            connect.close()

if __name__ == '__main__':
    # ywxtselect()
    # ywxtproc()
    ywxtupdeins()