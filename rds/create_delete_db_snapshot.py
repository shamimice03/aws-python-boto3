import json
import boto3
import datetime
import logging

REGION = 'ap-northeast-1'
INSTANCE_NAME = "test-db-1"
SNAPSHOT_PREFIX = "snap"

client = boto3.client('rds', region_name=REGION)
logging.basicConfig(level=logging.INFO)

def create_snapshot():
    today = datetime.datetime.now().date()
    new_snapshot_name = f"{SNAPSHOT_PREFIX}-{INSTANCE_NAME}-{today}"
    logging.info(f"Creating new snapshot: {new_snapshot_name}")
    try:
        response = client.create_db_snapshot(
            DBInstanceIdentifier= INSTANCE_NAME,
            DBSnapshotIdentifier= new_snapshot_name,
        )
        logging.info(f"Snapshot created: {response}")
    except Exception as e:
        logging.error(f"Error creating snapshot: {e}")
        
def delete_previous_snapshot():
    previous_day = datetime.datetime.now().date() - datetime.timedelta(days=1)
    previous_snapshot_name = f"{SNAPSHOT_PREFIX}-{INSTANCE_NAME}-{previous_day}"
    logging.info(f"Deleting previous snapshot: {previous_snapshot_name}")
    try:
        response = client.delete_db_snapshot(
            DBSnapshotIdentifier=previous_snapshot_name,
        )
        logging.info(f"Snapshot deleted: {response}")
    except Exception as e:
        logging.error(f"Error deleting snapshot: {e}")

# Calling
create_snapshot()
delete_previous_snapshot()