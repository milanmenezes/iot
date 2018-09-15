#!/usr/bin/python3
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

def on_message(client,userdata,msg):
	print("Topic:"+ msg.topic+"\nMessage: "+str(msg.payload.decode("utf-8")))
	print("Message_!:",msg.topic)
	if "GREEN" in msg.payload.decode("utf-8"):
		print("Green ON!")
		GPIO.output(11,1)
		GPIO.output(3,0)
		GPIO.output(5,0)
		time.sleep(0.5)
	elif "RED" in msg.payload.decode("utf-8"):
		print("Red ON!")
		GPIO.output(11,0)
		GPIO.output(3,1)
		GPIO.output(5,0)
		time.sleep(0.5)
	elif "WHITE" in msg.payload.decode("utf-8"):
		print("White ON!")
		GPIO.output(11,0)
		GPIO.output(3,0)
		GPIO.output(5,1)
		time.sleep(0.5)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT) #green
GPIO.setup(3,GPIO.OUT) #red
GPIO.setup(5,GPIO.OUT) #white
GPIO.setwarnings(False)

client = mqtt.Client("client-003")
client.connect("iot.eclipse.org",1883,60)
client.subscribe("milan51")
print("initialized")
client.on_message=on_message
client.loop_forever()

