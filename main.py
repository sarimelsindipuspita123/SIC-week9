import paho.mqtt.client as mqtt
from time import sleep

from oksi import averageOksi

# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = 'campuspedia'
password = 'qlue'
topic = "alatdiagnosa"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published \n")
	


client1 = mqtt.Client("nauval0")
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)

melsindi = averageOksi ()


status = float(melsindi[])
print(status)

for k in range(1,5):
	ret = client1.publish(topic,payload=status)
	sleep(1)