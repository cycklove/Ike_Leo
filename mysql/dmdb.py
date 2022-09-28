# -*- coding: utf-8 -*-

import sys,os
from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *
from win32api import MessageBox
from win32con import MB_OK, MB_ICONWARNING,MB_ICONINFORMATION
import pymysql

big = False
running = False

name = True
seed = False
choud = False

ip = '192.168.1.165'
zh = 'root'
mm = 'caokai3220251'
dbase = 'guanli'

cxsql = 'select name from cj_user where IS_ENABLE=1'


def connect_DBS(content):
    db = pymysql.connect(host=ip, user=zh, password=mm, database=dbase)
    cursor = db.cursor()
    cursor.execute(content)
    db.commit()
    cursor.close()
    db.close()


def name(): #获取数据库用户表并写入
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

    wordlist3 = []
    with open('name.txt') as f:
        for line in f.readlines():
            wordlist3.append(line.strip('\n'))  # strip('\n')去掉字符串中的'\n'
    name_list = wordlist3
    print("1",wordlist3)


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.RowLength = 0
        try:
            from os import path as pathq
            icon_path = pathq.join(pathq.dirname(__file__), './logo.ico')

            icon = QIcon()
            icon.addPixmap(QPixmap(icon_path))  # 这是对的。
            MainWindow.setWindowIcon(icon)
        except:
            pass
        # self.setupUi(MainWindow())

    def setupUi(self, MainWindow):
        #以下课直接粘贴生成的setupui代码
        MainWindow.setObjectName("点名器")
        MainWindow.resize(420, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(55, 50, 331, 71))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(55, 190, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(253, 190, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(11, 570, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 830, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(11, 370, 397, 191))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 340, 210, 21))
        self.label_2.setObjectName("label_2")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(11, 303, 111, 20))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(165, 303, 111, 20))
        self.pushButton_10.setObjectName("pushButton_10")

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(319, 303, 75, 20))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(550, 260, 89, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('3')
        self.lineEdit.setStyleSheet('''
        QListView, QLineEdit { 
            color: #D2D2D2; 
            background-color:#29292C;
            selection-color: #29292C; 
            border: 2px groove #29292C; 
            border-radius: 10px; 
            padding: 2px 4px; 
        } 
        QLineEdit:focus { 
            color: #D2D2D2; 
            selection-color: #29292C; 
            border: 2px groove #29292C; 
            border-radius: 10px; 
            padding: 2px 4px; 
        } 
        
                ''')
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(495, 260, 56, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet('color:white;background:#222225')
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(649, 240, 111, 61))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(30)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(473, 20, 353, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.listWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton.clicked.connect(self.start)

        self.pushButton_2.clicked.connect(self.stop)
        self.pushButton_5.clicked.connect(self.showHistory)
        # self.pushButton_10.clicked.connect(self.LinkDB)


        self.pushButton_7.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton_6.clicked.connect(self.showContinue)
        self.pushButton_7.clicked.connect(self.ten)
        self.pushButton_6.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.pushButton.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton_2.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton_3.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton_5.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')

        self.pushButton_10.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')

        self.pushButton_4.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        #以上可以修改
        self.centralwidget.setStyleSheet('''
             QWidget#centralwidget{
             color:#222225;
             background:#222225;
             border-top:1px solid #222225;
             border-bottom:1px solid #222225;
             border-right:1px solid #222225;
             border-left:1px solid #444444;
             border-top-left-radius:10px;
             border-top-right-radius:10px;
             border-bottom-left-radius:10px;
             border-bottom-right-radius:10px;
             }

             ''')
        self.close_widget = QtWidgets.QWidget(self.centralwidget)
        self.close_widget.setGeometry(QtCore.QRect(333, 0, 90, 30))
        self.close_widget.setObjectName("close_widget")
        self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
        self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格

        self.left_close = QPushButton("")  # 关闭按钮
        self.left_close.clicked.connect(MainWindow.close)
        self.left_visit = QPushButton("")  # 空白按钮
        self.left_visit.clicked.connect(MainWindow.big)
        self.left_mini = QPushButton("")  # 最小化按钮
        self.left_mini.clicked.connect(MainWindow.mini)
        self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.pushButton_3.clicked.connect(self.ren)
        self.label_2.setStyleSheet('color:white')

        self.scc = '''
         QListWidget{background-color:#2B2B2B;color:white}
         /*垂直滚动条*/
         QScrollBar:vertical{
             width:12px;
             border:1px solid #2B2B2B;
             margin:0px,0px,0px,0px;
             padding-top:0px;
             padding-bottom:0px;
         }
         QScrollBar::handle:vertical{
             width:3px;
             background:#4B4B4B;
             min-height:3;
         }
         QScrollBar::handle:vertical:hover{
             background:#3F3F3F;
             border:0px #3F3F3F;
         }
         QScrollBar::sub-line:vertical{
             width:0px;
             border-image:url(:/Res/scroll_left.png);
             subcontrol-position:left;
         }
         QScrollBar::sub-line:vertical:hover{
             height:0px;
             background:#222225;
             subcontrol-position:top;
         }
         QScrollBar::add-line:vertical{
             height:0px;
             border-image:url(:/Res/scroll_down.png);
             subcontrol-position:bottom;
         }
         QScrollBar::add-line:vertical:hover{
             height:0px;
             background:#3F3F3F;
             subcontrol-position:bottom;
         }
         QScrollBar::add-page:vertical{
             background:#2B2B2B;
         }
         QScrollBar::sub-page:vertical{
             background:#2B2B2B;
         }
         QScrollBar::up-arrow:vertical{
             border-style:outset;
             border-width:0px;
         }
         QScrollBar::down-arrow:vertical{
             border-style:outset;
             border-width:0px;
         }

         QScrollBar:horizontal{
             height:12px;
             border:1px #2B2B2B;
             margin:0px,0px,0px,0px;
             padding-left:0px;
             padding-right:0px;
         }
         QScrollBar::handle:horizontal{
             height:16px;
             background:#4B4B4B;
             min-width:20;
         }
         QScrollBar::handle:horizontal:hover{
             background:#3F3F3F;
             border:0px #3F3F3F;
         }
         QScrollBar::sub-line:horizontal{
             width:0px;
             border-image:url(:/Res/scroll_left.png);
             subcontrol-position:left;
         }
         QScrollBar::sub-line:horizontal:hover{
             width:0px;
             background:#2B2B2B;
             subcontrol-position:left;
         }
         QScrollBar::add-line:horizontal{
             width:0px;
             border-image:url(:/Res/scroll_right.png);
             subcontrol-position:right;
         }
         QScrollBar::add-line:horizontal:hover{
             width:0px;
             background::#2B2B2B;
             subcontrol-position:right;
         }
         QScrollBar::add-page:horizontal{
                    background:#2B2B2B;
         }
         QScrollBar::sub-page:horizontal{
                     background:#2B2B2B;
         }
        '''
        self.listWidget.setStyleSheet(self.scc)
        self.listWidget_2.setStyleSheet(self.scc)

        MainWindow.setWindowOpacity(0.95)  # 设置窗口透明度
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(132, 570, 100, 41))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.pushButton_8.clicked.connect(self.rename)
        self.pushButton_8.setText('重置名字文件')

    # def LinkDB(self):
    #     self.lkdb = Dbwindow()
    #     self.lkdb.show()

    def ten(self):
        num = self.lineEdit.text()
        print (num)
        num = int(num)
        if not num =='' and not num<=0 and not num>1000:
            if num > 30:
                reply = QtWidgets.QMessageBox.warning(self, u'警告', u'认真的吗，这么多', QtWidgets.QMessageBox.Yes)
            self.listWidget_2.clear()
            for i in range (0,int(num)):
                name = name_list[randint(0, len(name_list) - 1)]
                self.listWidget_2.addItem(name)
                self.listWidget.addItem(name)
                upsql = "update cj_user set IS_ENABLE=0 where name ='%s'" % name
                connect_DBS(content=upsql)
                while name in name_list:
                    name_list.remove(name)
        elif num =='':
            reply = QtWidgets.QMessageBox.warning(self, u'警告', u'请输入数字', QtWidgets.QMessageBox.Yes)
            self.listWidget_2.clear()
        elif num<0:
            #win32api.MessageBox(0, "你见过负数个人么???????", "通知", win32con.MB_OK | win32con.MB_ICONWARNING)
            reply = QtWidgets.QMessageBox.warning(self, u'警告', u'人数负数，输入有误！', QtWidgets.QMessageBox.Yes)
            self.listWidget_2.clear()
        elif num==0:
            #win32api.MessageBox(0, "人都被你吃了？？？", "通知", win32con.MB_OK | win32con.MB_ICONWARNING)
            reply = QtWidgets.QMessageBox.warning(self, u'警告', u'人数为0，输入有误！', QtWidgets.QMessageBox.Yes)
            self.listWidget_2.clear()
        elif num>1000:
            #win32api.MessageBox(0, "这么大？要不起~", "通知", win32con.MB_OK | win32con.MB_ICONWARNING)
            reply = QtWidgets.QMessageBox.warning(self, u'警告', u'人数超出限制，输入有误！', QtWidgets.QMessageBox.Yes)
            self.listWidget_2.clear()

    def ren(self):
        os.system('start ./name.txt')

    def retranslateUi(self, MainWindow):
            self.wide = 420
            self.high = 360
            _translate = QtCore.QCoreApplication.translate
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label.setText(_translate("MainWindow", "恭喜{}"))
            self.label.setStyleSheet('color:white')
            self.pushButton.setText(_translate("MainWindow", "开始"))
            self.pushButton_2.setText(_translate("MainWindow", "结束"))
            self.pushButton_3.setText(_translate("MainWindow", "打开名字文件"))
            self.pushButton_4.setText(_translate("MainWindow", "开gua选项"))
            self.label_2.setText(_translate("MainWindow", "点过的学号/姓名："))
            self.pushButton_5.setText(_translate("MainWindow", "查看点过的名字"))
            self.pushButton_10.setText(_translate("MainWindow", "配置数据库连接"))
            self.pushButton_6.setText(_translate("MainWindow", "连抽模式"))
            self.label_3.setText(_translate("MainWindow", "连抽人数"))
            self.pushButton_7.setText(_translate("MainWindow", "开始"))

    def showHistory(self):
        global seed
        if not seed:
            self.high = 656
            MainWindow.resize(self.wide,self.high)
            seed = True
        else:
            self.high = 360
            MainWindow.resize(self.wide, self.high)
            seed = False

    def showContinue(self):
        global choud
        if not choud:
            self.wide = 874
            MainWindow.resize(self.wide, self.high)
            choud = True
        else:
            self.wide = 420
            MainWindow.resize(self.wide, self.high)
            choud = False

    def gua(self):
        MessageBox(0, "就你也想开挂？？？", "~~~", MB_OK | MB_ICONWARNING)


    def setname(self):
        global running
        global name
        try:
            name = name_list[randint(0, len(name_list) - 1)]
            self.label.setText("恭喜 {}！".format(name))
            # upsql = "update cj_user set IS_ENABLE=0 where name ='%s'" % name
            # connect_DBS(content=upsql)
            #print (running)
        except:
            self.name()
            reply = QtWidgets.QMessageBox.warning(self, u'警告', u'发生错误', QtWidgets.QMessageBox.Yes)
            sys.exit()

    def rename(self):
        reply = QtWidgets.QMessageBox.question(self, u'警告', u'确定重置人员?', QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            czsql = "update cj_user set IS_ENABLE=1"
            connect_DBS(content=czsql) #重置数据库标识
            self.czname() #重置当前name_list数据
            self.listWidget.clear()
            self.listWidget_2.clear()
            MessageBox(0, "重置完成,", "通知", MB_OK | MB_ICONINFORMATION)
        else:
            pass

    def czname(self): #重置当前name_list数据
        print(name_list)
        widgetres = []
        # 获取listwidget中条目数
        count = self.listWidget.count()
        # 遍历listwidget中的内容
        for i in range(count):
            widgetres.append(self.listWidget.item(i).text())
            name_list.append(self.listWidget.item(i).text())
        print(name_list)

    def start(self):
        global running
        if running:
            print('running')
            pass
        else:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.setname)
            self.timer.start(50)
            running = 'True'

    def stop(self):
        global running
        if running:
            self.timer.stop()
            running = False
            self.listWidget.addItem(name)
            upsql = "update cj_user set IS_ENABLE=0 where name ='%s'" % name
            connect_DBS(content=upsql)
            while name in name_list:
                name_list.remove(name)
        else:

            reply = QtWidgets.QMessageBox.warning(self, u'警告', u'还没开始就想结束？', QtWidgets.QMessageBox.Yes)

    # 识别



# 重写MainWindow类
class MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def mousePressEvent(self, event):
        global big
        big = False

        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        if Qt.LeftButton and self.m_flag:
            self.setWindowState(Qt.WindowNoState)
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def big(self):
        global big
        print('最大化：{}'.format(big))
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False

    def close(self):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass


    def mini(self):

        self.showMinimized()

class Dbwindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("数据库配置")
        self.resize(380, 270)
        self.setObjectName("QWidget")
        self.setStyleSheet("#QWidget{color:#222225;background:#222225;border-top:1px solid #222225;border-bottom:1px solid #222225;border-right:1px solid #222225;border-left:1px solid #444444;border-top-left-radius:10px;border-top-right-radius:10px;border-bottom-left-radius:10px;border-bottom-right-radius:10px;}")

        self.label1 = QLabel('请输入数据库配置', self)
        self.label1.setGeometry(QtCore.QRect(75, 10, 331, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setObjectName("label")
        self.label1.setStyleSheet('color:white;background:#222225')

        self.qd = QPushButton('确定', self)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.qd.setFont(font)
        self.qd.setStyleSheet('''QPushButton{color:white;background:green;border-radius:5px;}QPushButton:hover{background:#6DDF6D;}''')
        self.qd.clicked.connect(self.getsj)

        self.ip_label = QLabel('输入IP:', self)
        self.ip_le = QLineEdit(self)
        self.zh_label = QLabel('用户名:', self)
        self.zh_le = QLineEdit(self)
        self.mm_label = QLabel('密码:', self)
        self.mm_le = QLineEdit(self)
        self.mm_le.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.db_label = QLabel('数据库名:', self)
        self.db_le = QLineEdit(self)

        self.ip_label.setStyleSheet('color:white;background:#222225')
        self.zh_label.setStyleSheet('color:white;background:#222225')
        self.mm_label.setStyleSheet('color:white;background:#222225')
        self.db_label.setStyleSheet('color:white;background:#222225')

        self.ip_label.setGeometry(QtCore.QRect(20, 45, 100, 30))
        self.ip_le.setGeometry(QtCore.QRect(72, 49, 200, 25))
        self.zh_label.setGeometry(QtCore.QRect(20, 90, 100, 30))
        self.zh_le.setGeometry(QtCore.QRect(72, 97, 200, 25))
        self.mm_label.setGeometry(QtCore.QRect(20, 135, 100, 30))
        self.mm_le.setGeometry(QtCore.QRect(72, 142, 200, 25))
        self.db_label.setGeometry(QtCore.QRect(10, 180, 100, 30))
        self.db_le.setGeometry(QtCore.QRect(72, 187, 200, 25))
        self.qd.setGeometry(QtCore.QRect(140, 225, 100, 30))


        self.close_widget = QtWidgets.QWidget(self)
        self.close_widget.setGeometry(QtCore.QRect(295, 0, 90, 30))
        self.close_widget.setObjectName("close_widget")
        self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
        self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格

        # self.left_close = QPushButton("")  # 关闭按钮
        # self.left_visit = QPushButton("")  # 空白按钮
        # self.left_mini = QPushButton("")  # 最小化按钮
        # self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        # self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
        # self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        # self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        # self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        # self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
        # self.left_close.setStyleSheet(
        #     '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        # self.left_visit.setStyleSheet(
        #     '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        # self.left_mini.setStyleSheet(
        #     '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        # self.left_close.clicked.connect(self.close)
        # self.left_visit.clicked.connect(self.big)
        # self.left_mini.clicked.connect(self.mini)

        #self.setWindowOpacity(0.95)  # 设置窗口透明度
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


    # def big(self):
    #     global big
    #     print('最大化：{}'.format(big))
    #     if not big:
    #         self.setWindowState(Qt.WindowMaximized)
    #         big = True
    #     elif big:
    #         self.setWindowState(Qt.WindowNoState)
    #         big = False
    #
    # def close(self):
    #     reply = QtWidgets.QMessageBox.question(self, '提示',
    #                                            "是否要退出程序？",
    #                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
    #                                            QtWidgets.QMessageBox.No)
    #     if reply == QtWidgets.QMessageBox.Yes:
    #         sys.exit()
    #     else:
    #         pass

    # def mini(self):
    #     self.showMinimized()

    def getsj(self):
        global ip
        global zh
        global mm
        global dbase
        ip = self.ip_le.text()
        zh = self.zh_le.text()
        mm = self.mm_le.text()
        dbase = self.db_le.text()
        name()
        self.close()

if __name__ == "__main__":
    name()
    wordlist3 = []
    with open('name.txt') as f:
        for line in f.readlines():
            wordlist3.append(line.strip('\n'))  # strip('\n')去掉字符串中的'\n'
    name_list = wordlist3
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()  # QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    lkdb = Dbwindow()
    ui.pushButton_10.clicked.connect(lkdb.show)
    MainWindow.show()
    sys.exit(app.exec_())

