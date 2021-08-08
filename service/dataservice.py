import json
import datetime
import serial
import sys

from domain.message import Message
from configuration.awsconfiguration import AwsConfig as configClient

aws_client = configClient.client('secretsmanager', 'sa-east-1')
endpoint = configClient.get_secret_endpoint()

iot = configClient("arduino", endpoint, "../.files/certificates/AmazonRootCA1.pem",
                   "../.files/certificates/private.pem.key",
                   "../.files/certificates/certificate.pem.crt")

connection = iot.iot_client()
connection.connect()


def publish(message):
    connection.publish("iot/soilDevice/1", json.dumps(message.__dict__), 1)
    print("Message was sent to AWS")


print("Collecting data from device...")
while True:
    try:
        arduino = serial.Serial('/dev/cu.usbserial-1420', baudrate=9600, timeout=None)
        record = arduino.readline()
        formatted_line = record.decode('UTF-8')
        print("Record:", formatted_line)

        data_message = Message("soil_device_1", "Mini Roseira", datetime.datetime.now().isoformat(), formatted_line)

        publish(data_message)

    except RuntimeError:
        connection.disconnect()
        print("An error occurred:", sys.exc_info()[0])
