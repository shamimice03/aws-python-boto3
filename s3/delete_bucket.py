import boto3
import json


bucketName="examplebuckaaetadad123"
client = boto3.client('s3')

# The `list_objects_v2` lists atmost 1000 objects. To delete all the buckets if it is more than 1000. 
# Use the following function

def empty_bucket(): 
    response = client.list_objects_v2(Bucket=bucketName)
    while response['KeyCount'] != 0:
        
        for item in response['Contents']:
            print(item['Key'])
            client.delete_object(Bucket=bucketName,Key=item['Key'])
            
        response = client.list_objects_v2(Bucket=bucketName)

# Calling the function
empty_bucket()

# Deleting Bucket Policy    
policy_delete_response = client.delete_bucket_policy(
    Bucket=bucketName,
)
print(policy_delete_response)

# Deleting the Bucket
bucket_delete_response = client.delete_bucket(
    Bucket=bucketName,
)
print(bucket_delete_response)
