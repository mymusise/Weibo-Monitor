from selenium import webdriver
from time import  sleep
import sys
from mail import *
from config import *

def init_(broswer,uid):
	broswer.get("http://weibo.com/login.php")
	broswer.get("http://weibo.com/u/"+uid+"?source=webim")
	weibos = broswer.find_elements_by_xpath("//div[@class='WB_feed WB_feed_profile']/div[@class='WB_cardwrap WB_feed_type S_bg2 ']")
	while len(weibos)==0:
		weibos = broswer.find_elements_by_xpath("//div[@class='WB_feed WB_feed_profile']/div[@class='WB_cardwrap WB_feed_type S_bg2 ']")
	print len(weibos)
	print weibos[1].get_attribute('mid')

	f=open('mid','w')
	for w in weibos:
		f.write(w.get_attribute('mid')+'\n')

def monitor(broswer,uid):
	broswer.get("http://weibo.com/u/"+uid+"?source=webim")
	weibos = broswer.find_elements_by_xpath("//div[@class='WB_feed WB_feed_profile']/div[@class='WB_cardwrap WB_feed_type S_bg2 ']")
	while len(weibos)==0:
		weibos = broswer.find_elements_by_xpath("//div[@class='WB_feed WB_feed_profile']/div[@class='WB_cardwrap WB_feed_type S_bg2 ']")
	print len(weibos)
	old_mid = open('mid','r').read().split('\n')
	for w in weibos:
		if w.get_attribute('mid') not in old_mid:
			print w.text
			mail_to(mailConfig['your_mail'],mailConfig['password'],mailConfig['mail_host'],mailConfig['mail_to'],'Weibo_Monitor',w.text.encode('utf-8'))
			midFile=open('mid','w')
			for w in weibos:
				midFile.write(w.get_attribute('mid')+'\n')
			break


def main(argv):
	if len(argv)==2:
		uid = argv[1]
		broswer = webdriver.Firefox()
		init_(broswer,uid)
		while 1:
			monitor(broswer,uid)
			sleep(10)
	print argv


if __name__ == '__main__':
	main(sys.argv)