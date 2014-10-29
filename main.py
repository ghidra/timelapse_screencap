import os
import sys
import threading
import time
from screencap import screencap

seq=0
save_path=os.getcwd()
save_name="screencap"
interval=1

def main(kwargs):

	#usage
	#first is the path
	#second is the filename
	#third is the interval in seconds

	global save_path
	global save_name
	global interval

	if(len(kwargs)>1):
		if(kwargs[1]!=""):
			save_path = kwargs[1]
	if(len(kwargs)>2):
		if(kwargs[2]!=""):
			save_name = kwargs[2] 
	if(len(kwargs)>3):
                if(kwargs[3]!=""):
                        interval = kwargs[3]


	#screencap(save_path,save_name+str(seq),1)
	capture()

def capture():
	global seq
	global save_path
	global save_name
	global interval
	
	#print "running:"+str(seq)
	screencap(save_path,save_name+str(seq))
	seq=seq+1
	threading.Timer(interval, capture).start()

# start calling f now and every 60 sec thereafter

if __name__ == "__main__":
  main(sys.argv)

