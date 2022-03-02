import smtplib
from email.mime.text import MIMEText
from email.header import Header
import cx_Oracle as oracle
##以下解决Linux下SQL返回中文显示???的问题
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

class IkeSendMail:

    def __init__(self):
        pass

    def connect_DBS(self,content,bs):

        if bs == 1 :
            db = oracle.connect('dim/dim123@192.168.1.94:1521/dws')
            cursor = db.cursor()
            cursor.execute(content)
            data = cursor.fetchone()
            db.commit()
            cursor.close()
            db.close()
            return data
        elif bs == 2:
            db = oracle.connect('dim/dim123@192.168.1.94:1521/dws')
            cursor = db.cursor()
            cursor.execute(content)
            db.commit()
            cursor.close()
            db.close()

    def send_mail(self):
        try:
            content = "select ID,CREATE_TIME,TAGS,HOST,DB_TYPE,ALARM_ITEM,MESSAGE,JKLX  from (select ID,CREATE_TIME,TAGS,HOST,DB_TYPE,ALARM_ITEM,MESSAGE,JKLX from alarm where create_time>trunc(sysdate,'dd') and send_mail=0 order by id desc) a where ROWNUM=1"  # 需要执行的语句
            data = self.connect_DBS(content=content,bs=1)
            #print(data)
            rtdd1 = (data[0])
            rtdd2 = (data[1])
            rtdd3 = (data[2])
            rtdd4 = (data[3])
            rtdd5 = (data[4])
            rtdd6 = (data[5])
            rtdd7 = (data[6])
            rtdd8 = (data[7])

            msg = ["告警时间：%s"%rtdd2 ,"标识：%s"%rtdd3,"主机：'%s'"%rtdd4,"数据库类型：'%s'"%rtdd5,"告警原因：%s"%rtdd6,
                   "告警说明：%s" %rtdd7,"告警来源：%s"%rtdd8]
            print(msg)

            mail_host = "smtp.163.com"  # 设置服务器
            mail_user = "saiyuyu3@163.com"  # 用户名
            mail_pass = "TZDRBINGWJFZZSGE"  # 口令

            sender = 'saiyuyu3@163.com'
            receivers = ['saiyuyu3@163.com','283457474@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

            message = MIMEText("<br/>".join(msg), 'html', 'utf8')
            message['From'] = "Ike_Leo"
            message['To'] = ";".join(receivers)

            subject = '合并监控告警信息！'
            message['Subject'] = Header(subject, 'utf8')

            for i in receivers:
                try:
                    smtpObj = smtplib.SMTP()
                    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
                    smtpObj.login(mail_user, mail_pass)
                    smtpObj.sendmail(sender, i, message.as_string())
                    print("邮件发送成功")
                except smtplib.SMTPException:
                    print("Error: 无法发送邮件")
            return  rtdd1
        except Exception as e:
            print("没有告警事项。")

        ##标记为已发送
    def upsendmail(self,getid):
        if getid:
            content2 = "update alarm set send_mail=1 where id = %s" %getid
            # print(content2)
            self.connect_DBS(content=content2,bs=2)
        else:
            pass


if __name__ == '__main__':
    sm = IkeSendMail()
    getid = sm.send_mail()
    sm.upsendmail(getid=getid)