import RPi.GPIO as GPIO
import time

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

l=[1,0,0]
while True:
	print l
	GPIO.output(3,l[0])
	time.sleep(0.3)
	GPIO.output(5,l[1])
	time.sleep(0.3)
	GPIO.output(11,l[2])
	time.sleep(0.3)
	l=[l[-1]]+l[:-1]
#	time.sleep(0.6)
