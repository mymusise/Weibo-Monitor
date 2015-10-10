import logging
from logging.handlers import RotatingFileHandler

def __init__():
	pass

def initLog():
	LOG_FILENAME='log/monitor.log'
	my_logger = logging.getLogger('MyLogger') 
	my_logger.setLevel(logging.DEBUG) 
	handler = logging.handlers.RotatingFileHandler(
				LOG_FILENAME,
				maxBytes=512*1024, 
				backupCount=5, 
				) 
	formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s') 
	handler.setFormatter(formatter)

	my_logger.addHandler(handler)
	return my_logger