import smtplib
from email.mime.text import MIMEText
from random import Random
from config import *
#################
#example
# mail_host = 'smtp.163.com'
# your_user = 'server_ping@163.com'
# mail_pwd = 'yourpasswd'
# mail_to_user1 = "someone@outlook.com"
# mail_cc = "someone@gmail.com"
# your_content="Hello world"
##
#################
def random_str(randomlength=8):
	str = ''
	chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
	length = len(chars) - 1
	random = Random()
	for i in range(randomlength):
		str+=chars[random.randint(0, length)]
	return str

def mail_to(your_user,your_passwd,mail_host,mail_to_user1,title,your_content):
	random_s=random_str()
	content = your_content+'\n\n\n'+random_s
	msg = MIMEText(content)
	msg['From'] = your_user
	msg['To']=mail_to_user1
	msg['Subject'] = title+'\t'+random_s
	s = smtplib.SMTP()
	s.connect(mail_host)
	s.login(your_user,your_passwd)
	s.sendmail(your_user,[mail_to_user1],msg.as_string())
	s.close()
	pass

def main():
	mail_to(mailConfig['your_mail'],mailConfig['password'],mailConfig['mail_host'],mailConfig['mail_to'],'Server_down','Hello world')
	pass

if __name__ == '__main__':
	main()

