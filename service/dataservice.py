import json
import datetime
import serial
import os

from domain.message import Message
from config.awsconfiguration import AwsConfig

print("Collecting data from device...")

aws_client = AwsConfig.client('secrets-manager', 'sa-east-1')
iot = AwsConfig('arduino', 'josajs', 'ca', 'key', 'certificate')

connection = iot.iot_client()
connection.connect()

print("Sending to IoT core")




