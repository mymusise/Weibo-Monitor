from selenium import webdriver
from time import  sleep
import sys
from mail import *
from config import *

def delay(time):
	for i in range(time):
		for j in range(1000):
			for k in range(500):
				a=100*100

def init_(broswer,uid):
	broswer.get("http:/m.weibo.cn/u/"+uid)
	weibos = broswer.find_elements_by_xpath("//div[@class='card-list']/div[@class='card card9 line-around']")
	while len(weibos)==0:
		weibos = broswer.find_elements_by_xpath("//div[@class='card-list']/div[@class='card card9 line-around']")
	print len(weibos)
	print weibos[1].get_attribute('data-jump')

	f=open('mid','w')
	for w in weibos:
		f.write(w.get_attribute('data-jump')+'\n')

def monitor(broswer,uid):
	broswer.get("http://m.weibo.cn/u/"+uid+"?source=webim")
	weibos = broswer.find_elements_by_xpath("//div[@class='card-list']/div[@class='card card9 line-around']")
	while len(weibos)==0:
		weibos = broswer.find_elements_by_xpath("//div[@class='card-list']/div[@class='card card9 line-around']")
	print len(weibos)
	old_mid = open('mid','r').read().split('\n')
	for w in weibos:
		if w.get_attribute('data-jump') not in old_mid:
			print w.text
			mail_to(mailConfig['your_mail'],mailConfig['password'],mailConfig['mail_host'],mailConfig['mail_to'],'Weibo_Monitor',w.text.encode('utf-8'))
			delay(monitorTime)
			midFile=open('mid','w')
			for w in weibos:
				midFile.write(w.get_attribute('data-jump')+'\n')
			break


def main(argv):
	if len(argv)==2:
		uid = argv[1]
		broswer = webdriver.PhantomJS()
		init_(broswer,uid)
		while 1:
			monitor(broswer,uid)
			sleep(10)
	print argv


if __name__ == '__main__':
	main(sys.argv)