import boto3
import logging
import botocore 

client = boto3.client('s3')
bucketName="examplebuckaaetadad123"

try:
    response = client.create_bucket(
            Bucket=bucketName,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-northeast-1',
            },
        )
    print(response)
    
except botocore.errorfactory.BucketAlreadyOwnedByYou as error:
    logging.error("BucketAlreadyOwnedByYou")
