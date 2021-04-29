import paho.mqtt.client as mqtt
import read_from_file
from time import sleep
mqtt_username = "amit"
mqtt_password = "amit123"
mqtt_topic = "value"
mqtt_broker_ip = "192.168.1.18"

client = mqtt.Client()
client.username_pw_set(mqtt_username, mqtt_password)
unsent_data = []

if __name__=='__main__':
    client.connect(mqtt_broker_ip, 1883)
    data_from_file = read_from_file.read()
    print(data_from_file)
    client.publish(mqtt_topic, data_from_file[0]['Value'])
    while True:
        print("sending")
        for count in range(len(data_from_file)):
            client.publish(mqtt_topic,data_from_file[count]['Value'])
            sleep(1)
            print("sent: ",mqtt_topic,data_from_file[count]['Value'])
