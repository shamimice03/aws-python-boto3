import json
import boto3

region = 'ap-northeast-1'
client = boto3.client('ec2', region_name=region)

response = client.delete_snapshot(
    SnapshotId= 'snap-03d56ab0a90d3311f'
)

print(response)