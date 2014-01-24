from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from email.header import Header


if __name__ == "__main__":
    fromadrr = "huyajun1989@126.com"
    toadrr = "snailhu@yahoo.com"

    msg = MIMEMultipart()
    msg['From']= fromadrr
    msg['To']= ";".join(toadrr)
    msg['Subject']=Header("from suzhou snail ")

    body = "http://www.baidu.com"
    msg.attach(MIMEText(body,'plain','utf-8'))
    server = smtplib.SMTP('smtp.126.com','25')
    # server.login("dongshiyue1009@qq.com","")
    server.login('huyajun1989@126.com', 'huyajun1989122')
    server.sendmail(fromadrr, toadrr,msg.as_string())
    print 'finish'
    server.quit()
