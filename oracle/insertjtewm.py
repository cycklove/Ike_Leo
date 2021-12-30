from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.ttk
import cx_Oracle as oracle

def insertjtinfo():

    try:
        db = oracle.connect('ddqs/ddqs2016@192.168.1.92:1521/ddqs')

        gcbm = e1.get()
        wlbm = e2.get()
        khbm = e3.get()
        wxm  = e4.get()

        len1 = len(gcbm)
        len2 = len(wlbm)
        len3 = len(khbm)
        len4 = len(wxm)

        row_data = []

        if len1 == 0:
            lb5["fg"] = "RED"
            fk = lb5["text"] = '工厂编码不能为空!'
            return fk
        elif len2 == 0:
            lb5["fg"] = "RED"
            fk = lb5["text"] = '物料编码不能为空!'
            return fk
        elif len3 == 0:
            lb5["fg"] = "RED"
            fk = lb5["text"] = '客户编码不能为空!'
            return fk
        elif len4 == 0:
            lb5["fg"] = "RED"
            fk = lb5["text"] = '箱码不能为空!'
            return fk
        else:

            cursor = db.cursor()
            sql1= 'select code,name from org_stockorg where code = %s'%gcbm
            cursor.execute(sql1)
            # row = c.fetchall()
            # for i in row:
            #     print(i)+
            row = cursor.fetchone()
            while row:
                print(row)
                row_data.append(row[0])
                row_data.append(row[1])
                row = cursor.fetchone()
            # print("执行成功sql: %s"%sql_item)

            sql2 = 'select code,name from bd_material_v where code = %s'%wlbm
            cursor.execute(sql2)
            # row = c.fetchall()
            # for i in row:
            #     print(i)+
            row2 = cursor.fetchone()
            while row2:
                print(row2)
                row_data.append(row2[0])
                row_data.append(row2[1])
                row2 = cursor.fetchone()

            row_data.append(khbm)
            row_data.append(wxm)

            print(row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5])

            sql3 = "INSERT INTO serial_info(ID,OUT_SERIAL_NO,CENTRYPT_NO,IN_SERIAL_NO,FACTORY_CODE,FACTORY_NAME,ITEM_CODE,ITEM_NAME,WEB,STATUS,BATCH_NO,QUALITY_INSPECTOR,MOISTURE,ACID_NUMBER,RESIDUAL_SOLVENT,COLOR_ATION,QUERY_TOTAL,CREATE_BY,CREATE_DATE,UPDATE_BY,UPDATE_DATE,REMARKS,DEL_FLAG,SCRQ,CKDH,KHBM,XM)VALUES(sys_guid(),'~','~','~',:1,:2,:3,:4,'http://c.ddqly.cn',1,'202108250003','刘丰','.03','.69','未检出','R1.0Y35.0',0,1,SYSDATE,1,SYSDATE,'实施人员写入',0,sysdate,'666666666666',:5,:6)"
            data = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5])

            cursor.execute(sql3, data)  # 执行sql语句

            row_data = []
            lb5["fg"] = "green"
            lb5["text"] = '插入成功!'
            db.commit()
        cursor.close()
        db.close()
    except:
        lb5["fg"] = "RED"
        fk = lb5["text"] = '必须输入正确的工厂编码和物料编码！'
        return fk

baseframe = tkinter.Tk()
baseframe.geometry("800x600")
baseframe.wm_title("道道全集团二维码补码")

photo = tkinter.PhotoImage(file="bg.gif")  # file：t图片路径

lb3 = tkinter.Label(baseframe, text="", justify=tkinter.LEFT, image=photo, compound=tkinter.CENTER, font=("微软雅黑",16))
lb3.place(x=1, y=1, width=800, height=600)

lb0= tkinter.Label(baseframe, text="请输入以下必要信息", bg="white", fg="green", font=("微软雅黑", 18))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb0.pack()

lb1= tkinter.Label(baseframe, text="工厂编码：", bg="white", fg="black", font=("微软雅黑", 16))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb1.place(x=300,y=45)

e1 = tkinter.Entry(baseframe, width=20, insertbackground='black', highlightthickness=1, fg="black",font=("微软雅黑", 12))
# e1.grid(row=0,column=1,stick=tkinter.E)
#e1.bind("<Return>", insertjtinfo)
e1.place(x=400,y=50)

lb2= tkinter.Label(baseframe, text="物料编码：", bg="white", fg="black", font=("微软雅黑", 16))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb2.place(x=300,y=85)

e2 = tkinter.Entry(baseframe, width=20, insertbackground='black', highlightthickness=1, fg="black",font=("微软雅黑", 12))
# e1.grid(row=0,column=1,stick=tkinter.E)
e2.place(x=400,y=90)

lb3= tkinter.Label(baseframe, text="客户编码：", bg="white", fg="black", font=("微软雅黑", 16))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb3.place(x=300,y=132)

e3 = tkinter.Entry(baseframe, width=20, insertbackground='black', highlightthickness=1, fg="black",font=("微软雅黑", 12))
# e1.grid(row=0,column=1,stick=tkinter.E)
e3.place(x=400,y=138)

lb4= tkinter.Label(baseframe, text="箱码：", bg="white", fg="black", font=("微软雅黑", 16))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb4.place(x=340,y=170)

e4 = tkinter.Entry(baseframe, width=20, insertbackground='black', highlightthickness=1, fg="black",font=("微软雅黑", 12))
# e1.grid(row=0,column=1,stick=tkinter.E)
e4.place(x=400,y=175)

btn = tkinter.Button(baseframe, text="确定插入", command=insertjtinfo, fg="green", font=("微软雅黑", 18), highlightthickness=1)
# btn.grid(row=2,column=1,stick=tkinter.E)
#btn.pack()
btn.place(x=350,y=210)

# lb3 = tkinter.Label(baseframe, text="",image=photo,compound = "center")

lb5 = tkinter.Label(baseframe, text="", bg="white", fg="green", font=("微软雅黑", 20))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb5.place(x=230, y=300)

lb4 = tkinter.Label(baseframe, text="©Develop:Ike...Leo", bg="white", fg="green", font=("微软雅黑", 18))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb4.place(x=240, y=500)

<<<<<<< HEAD
baseframe.mainloop()
=======
baseframe.mainloop()
>>>>>>> origin/Ike_leo
