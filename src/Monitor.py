from selenium import webdriver
from time import  sleep
from mail import *
from config import *
import log
class Monitor():
	def __init__(self,uid):
		self.uid = uid
		self.broswer  = webdriver.Firefox()
		self.logger   = log.initLog()
		self.tmpFile  = "tmp/mid"
		self.link	  = "http:/m.weibo.cn/u/"+uid
		self.cardPath = "//div[@class='card-list']/div[@class='card card9 line-around']"

	def delay(self,time):
		for i in range(time):
			for j in range(1000):
				for k in range(500):
					a=100*100

	def init_(self):
		self.broswer.get(self.link)
		weibos = self.broswer.find_elements_by_xpath(self.cardPath)
		while len(weibos)==0:
			weibos = self.broswer.find_elements_by_xpath(self.cardPath)
			self.delay(monitorTime)

		f=open(self.tmpFile,'w')
		for w in weibos:
			f.write(w.get_attribute('data-jump')+'\n')

	def monitor(self):
		self.broswer.get(self.link)
		weibos = self.broswer.find_elements_by_xpath(self.cardPath)
		while len(weibos)==0:
			self.broswer.get(self.link)
			weibos = self.broswer.find_elements_by_xpath(self.cardPath)
		self.logger.info(weibos[0].get_attribute('data-jump'))
		old_mid = open(self.tmpFile,'r').read().split('\n')
		for w in weibos:
			if w.get_attribute('data-jump') not in old_mid:
				print w.text
				mail_to(mailConfig['your_mail'],mailConfig['password'],mailConfig['mail_host'],mailConfig['mail_to'],'Weibo_Monitor',w.text.encode('utf-8'))
				self.delay(monitorTime)
				midFile=open(self.tmpFile,'w')
				for w in weibos:
					midFile.write(w.get_attribute('data-jump')+'\n')
				break

	def run(self):
		self.init_()
		while 1:
			self.monitor()
			sleep(monitorTime)

def main(argv):
	if len(argv)==2:
		uid = argv[1]
		monitor = Monitor(uid)
		monitor.run()

