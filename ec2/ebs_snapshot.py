import json
import boto3

region = 'ap-northeast-1'
client = boto3.client('ec2', region_name=region)

response = client.stop_instances(
    InstanceIds=[
        'i-0f98e256d6c2e985a',
    ]
)

print(response)