import src.Monitor
import sys
def main(argv):
	if len(argv)==2:
		uid = argv[1]
		monitor = src.Monitor.Monitor(uid)
		monitor.run()

if __name__ == '__main__':
	main(sys.argv)