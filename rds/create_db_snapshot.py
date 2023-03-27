import json
import boto3
import datetime

region = 'ap-northeast-1'
client = boto3.client('rds', region_name=region)

instance_name = "test-db-1"
today = datetime.datetime.now().date()
previous_day = today- datetime.timedelta(days=1)

print(previous_day)
snapshot_name = f"snap-{instance_name}-{today}"
print(snapshot_name)

response = client.create_db_snapshot(
    DBInstanceIdentifier= instance_name,
    DBSnapshotIdentifier= snapshot_name,
)

print(response)