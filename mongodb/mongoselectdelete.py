import os
import sys
import string
import pymongo
import random
import pandas as pd
import tkinter

host='192.168.1.113'
port=27017
user='ddq-api'
passwd='1qaz@WSX'
dbname='ddq_api'

def selectmongo():
    try:
        connect = pymongo.MongoClient(host,int(port))
        db = connect[dbname]
        db.authenticate(user,passwd)
        print("MongoDB server connect success!")

        collection = db['integralRecord']

        xm = e1.get()

        count = collection.find_one({'sku':{'$in':[xm]}},{'sku':True,'storeName':True,'_id':False})

        if count != None:
            array = list(collection.find({'sku':{'$in':[xm]}},{'sku':True,'storeName':True,'_id':False}))
            type(array)
            df = pd.DataFrame(array)
            # df = collection.find_one({'sku':{'$in':[xm]}},{'sku':True,'storeName':True,'_id':False})

            lb3["fg"] = "black"
            lb3["text"] = df
        else:
            lb3["fg"] = "RED"
            lb3["text"] = '没有此码！'

    except:
        lb3["fg"] = "RED"
        lb3["text"] = '没有此码！'

def deletemongo():
    try:
        connect = pymongo.MongoClient(host,int(port))
        db = connect[dbname]
        db.authenticate(user,passwd)
        print("MongoDB server connect success!")

        collection = db['integralRecord']

        xm = e2.get()

        cd = len(xm)

        if cd > 0:

            count = collection.find_one({'sku': {'$in': [xm]}}, {'sku': True, 'storeName': True, '_id': False})

            if count != None:
                collection.delete_many({'sku':{'$in':[xm]}})

                lb3["fg"] = "green"
                lb3["text"] = '删除成功!'
            else:
                lb3["fg"] = "RED"
                lb3["text"] = '没有此码！'
        else:
            fk = lb3["text"] = '必须输入需要删除的码!'
            return fk

    except:
        lb3["fg"] = "RED"
        lb3["text"] = '没有此码！'


baseframe = tkinter.Tk()
baseframe.geometry("800x600")
baseframe.wm_title("道道全信息中心MongoDB小程序查删码")

photo = tkinter.PhotoImage(file="bg.gif")  # file：t图片路径

lb3 = tkinter.Label(baseframe, text="", justify=tkinter.LEFT, image=photo, compound=tkinter.CENTER, font=("微软雅黑",16))
lb3.place(x=1, y=1, width=800, height=600)

lb1 = tkinter.Label(baseframe, text="请输入要查询的码:", bg="white", fg="green", font=("微软雅黑", 18))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb1.pack()

e1 = tkinter.Entry(baseframe, width=50, insertbackground='green', highlightthickness=1, fg="green")
# e1.grid(row=0,column=1,stick=tkinter.E)
e1.bind("<Return>", selectmongo)
e1.pack()

btn = tkinter.Button(baseframe, text="确定", command=selectmongo, fg="green", font=("微软雅黑", 18), highlightthickness=1)
# btn.grid(row=2,column=1,stick=tkinter.E)
btn.pack()

'''******************************'''
lb2 = tkinter.Label(baseframe, text="请输入要删除的码:", bg="white", fg="red", font=("微软雅黑", 18))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb2.pack()

e2 = tkinter.Entry(baseframe, width=50, insertbackground='red', highlightthickness=1, fg="red")
# e1.grid(row=0,column=1,stick=tkinter.E)
e2.pack()

btn2 = tkinter.Button(baseframe, text="确定", command=deletemongo, fg="red", font=("微软雅黑", 18), highlightthickness=1)
# btn.grid(row=2,column=1,stick=tkinter.E)
btn2.pack()

# lb3 = tkinter.Label(baseframe, text="",image=photo,compound = "center")

lb4 = tkinter.Label(baseframe, text="©Develop:Ike...Leo", bg="white", fg="green", font=("微软雅黑", 18))
# lb1.grid(row=0,column=0,stick=tkinter.W)
lb4.place(x=240, y=500)

baseframe.mainloop()

