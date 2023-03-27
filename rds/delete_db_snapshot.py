import json
import boto3
import datetime

region = 'ap-northeast-1'
client = boto3.client('rds', region_name=region)

instance_name = "test-db-1"
today = datetime.datetime.now().date()
previous_day = today- datetime.timedelta(days=1)
previous_snapshot_name = f"snap-{instance_name}-{previous_day}"
print(previous_snapshot_name)

response = client.delete_db_snapshot(
    DBSnapshotIdentifier=previous_snapshot_name,
)

print(response)