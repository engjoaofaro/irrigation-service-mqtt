import json
import datetime
import serial
import os
import time as t

from domain.message import Message
from configuration.awsconfiguration import AwsConfig

print("Collecting data from device...")

aws_client = AwsConfig.client('secretsmanager', 'sa-east-1')
endpoint = AwsConfig.get_secret_endpoint()
iot = AwsConfig("arduino", endpoint, "../.files/certificates/AmazonRootCA1.pem",
                "../.files/certificates/private.pem.key",
                "../.files/certificates/certificate.pem.crt")

connection = iot.iot_client()
connection.connect()

for i in range(10):
    connection.publish("test/testing", i+1, 1)
    print("Published")
    t.sleep(0.1)

print("Sending to IoT core")

connection.disconnect()




