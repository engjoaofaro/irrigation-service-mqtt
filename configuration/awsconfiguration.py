import boto3
import base64
from botocore.exceptions import ClientError

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

    @staticmethod
    def get_secret_endpoint():

        secret_name = "app/iot/endpoint"
        region_name = "sa-east-1"

        session = boto3.session.Session()
        client = session.client(
            'secretsmanager',
            region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                raise e
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise e
        else:
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                return secret
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                return decoded_binary_secret
