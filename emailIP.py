import smtplib
from email.mime.text import MIMEText
import time
import socket
import subprocess

#content
mail_text = 'hello this is an email from 163'
#sender
mail_sender = 'myraspberrypi@163.com'
mail_receiver = 'ivincentlin@gmail.com'

#very linux specific
arg = 'ip route list'
p = subprocess.Popen(arg,shell=True,stdout = subprocess.PIPE)
data = p.communicate()
spilt_data = data[0].split()
ipadder = spilt_data[spilt_data.index('src')+1]
my_ip = 'the IP of raspberryPi is %s' % ipadder
print my_ip


msg = MIMEText(my_ip)
msg['Subject'] = 'the IP address of raspberryPi'
msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S %z')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login('xxxxxx@163.com','xxxxxxx')


smtp.sendmail(mail_sender,mail_receiver,msg.as_string())
smtp.quit()
print 'ok'

