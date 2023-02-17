"""EE 250L Lab 04 Starter Code
Run vm_pub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("cnlei/start")
    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("cnlei/start", on_message_from_ipinfo)
    # client.message_callback_add("cnlei", pong)

# Default callback
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom callback.
def on_message_from_ipinfo(client, userdata, message):
    newInt = int(message.payload.decode()) +1
    print("Custom callback  - Count "+ f"{newInt}")
    client.publish("cnlei/cont", f"{newInt}")
    time.sleep(2)

#def pong(client, message):
    
if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    client.connect(host="172.20.10.5", port=1883, keepalive=60)

    client.loop_forever()

