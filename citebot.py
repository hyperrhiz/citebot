import random
import time
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

#line = random.choice(open('citations.txt').readlines())
#print(line)
#printer.println(line)
#printer.feed(1)


while True:
	def generate_post():
		with open('cleaned.txt') as f:
	
			cite = random.choice(list(f))
    		printer.println(cite)
    		printer.feed(3)
    		time.sleep(10)
		return cite

	generate_post()