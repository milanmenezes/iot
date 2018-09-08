import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BOARD)
PIN_TRIGGER=16
PIN_ECHO=18

url='https://api.thingspeak.com/update'
key='X2RGZDZOPRMDM7R5'

GPIO.setup(PIN_TRIGGER,GPIO.OUT)
GPIO.setup(PIN_ECHO,GPIO.IN)
try:
    while True:
        GPIO.output(PIN_TRIGGER,GPIO.LOW)
#print "Waiting for sensor to settle"

        time.sleep(2)

#print "Calculating distance"
        GPIO.output(PIN_TRIGGER,GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER,GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time=time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time=time.time()


        pulse_duration=pulse_end_time - pulse_start_time
        distance= round(pulse_duration *17150,2)

        print "Distance:", distance,"cm"
        if distance<10:
                data={'api_key':key,'field1':distance}
	        requests.post(url,data)
                #time.sleep(5)
finally:
    GPIO.cleanup()
