import pymssql

def c82select():

    conn = pymssql.connect('192.168.6.203','sa','AAAaaa123','cyls1')

    cursor = conn.cursor()

    cursor.execute("select id,convert(nvarchar,mc) from tb_gsjg where id = dbo.f_get_gsjg()")
    row = cursor.fetchall()
    for i in row:
        print(i)
    # conn.commit()
    cursor.close()
    conn.close()

def c82proc():

    conn = pymssql.connect('192.168.6.203','sa','AAAaaa123','cyls1')

    cursor = conn.cursor()

    cursor.execute("exec p_cb_c82_jbzl")
    # row = cursor.fetchall()
    # for i in row:
    #     print(i)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # c82select()
    c82proc()