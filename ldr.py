#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import requests
import datetime as d

GPIO.setmode(GPIO.BOARD)

pin_to_circuit = 18
url='https://api.thingspeak.com/update'
key='LWE2UWNJ3X1PI519'

def rc_time(pin_to_circuit):
	count = 0
	GPIO.setup(pin_to_circuit, GPIO.OUT)
	GPIO.output(pin_to_circuit, GPIO.LOW)
	time.sleep(0.1)
	GPIO.setup(pin_to_circuit, GPIO.IN)
	while(GPIO.input(pin_to_circuit) == GPIO.LOW):
		count += 1
	#print(count)
	temp=int(open('/sys/class/thermal/thermal_zone0/temp').read())
	data={'api_key':key,'field2':temp,'field3':count,'field1':d.datetime.now()}
	requests.post(url,data)
	return count
try:
	while True:
		print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()
