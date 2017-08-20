import paho.mqtt.client as mqtt

topicAp = "/iotgym/fromgw"

def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
	message = str(msg.payload)[2:-1]	

	print (message)


def main():
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message

	try:
		client.connect("117.16.136.173", 1883, 30)
		# client.connect("117.16.136.159", 1883, 30)
		print("Connection on Success")

		client.subscribe(topicAp)
		print("Subscribed to - " + topicAp)
		
		# client.publish(“hello/world”, “Hello, World!”)

		client.loop_forever()
		
	except Exception as e:
		print(e)
		print("Connection on Failure")

if __name__ == '__main__':
	main()
	