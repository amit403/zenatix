import csv
import paho.mqtt.client as mqtt
import time
    
client = mqtt.Client()
client.username_pw_set("amit", "amit123")

def on_message(client, userdata, message):
    time.sleep(1)
    print("received =",str(message.payload.decode("utf-8")))
    with open('data.csv', mode='a') as data_file:
        fieldnames = ['Value']
        write = csv.DictWriter(data_file, fieldnames=fieldnames)
        write.writerow({'Value':str(message.payload.decode("utf-8"))})
    

if __name__ == "__main__":
    client.connect("192.168.1.18", 1883)
    client.on_message=on_message
    client.loop_start()
    client.subscribe("value")
    
    while(True):
        pass
