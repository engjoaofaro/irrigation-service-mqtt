import boto3
import AWSIoTPythonSDK.MQTTLib as awsIot


class AwsConfig:

    def __init__(self, name_device, endpoint, ca_file_path, key_path, certificate_path):
        self.__name_device = name_device
        self.__endpoint = endpoint
        self.__ca_file_path = ca_file_path
        self.__key_path = key_path
        self.__certificate_path = certificate_path

    @staticmethod
    def client(aws_service, region):
        return boto3.client(aws_service, region)

    def __build_iot_client(self):
        client = awsIot.AWSIoTMQTTClient(self.__name_device)
        client.configureEndpoint(self.__endpoint, 8883)
        client.configureCredentials(self.__ca_file_path, self.__key_path, self.__certificate_path)

        return client

    def iot_client(self):
        return self.__build_iot_client()
