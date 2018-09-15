import time
import paho.mqtt.client as paho
broker="iot.eclipse.org"
def on_message(client,userdata,message):
	time.sleep(1)
	print("receive message = ",str(message.payload.decode("utf-8")))

client=paho.Client("client-003")
client.on_message=on_message
print(client.on_message)


print("Connecting to broker",broker)
client.connect(broker,1883,60)
client.loop_start()
print("Subscribing")
client.subscribe("milan51")
time.sleep(2)
print("publishing")
client.publish("milan51","GREEN")
time.sleep(4)

client.disconnect()
client.loop_stop()
