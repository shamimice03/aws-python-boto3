import json
import boto3

region = 'ap-northeast-1'
client = boto3.client('ec2', region_name=region)

response = client.terminate_instances(
    InstanceIds=[
        'i-0958d28ad2f10aae2',
    ],
)

print(response)