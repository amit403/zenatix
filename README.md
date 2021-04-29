# zenatix
This repo consist of two codes.. one is server and other is edge.

file name iot.py : main program which fetches the data from the csv file and publish to MQTT broker.
          read_from_file: this program reads the data from CSV file
          data_receive : this file will run on Raspberry Pi which is taken as  MQTT broker
          
I had configured MQTT broker on raspberry pi and created two program to share the data.

