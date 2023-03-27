import boto3

client = boto3.client('s3')

bucketName = "mytestbuckte1054589"
keyName ="greetings"

response = client.put_object(
        Body="Hello folks",
        Bucket=bucketName,
        Key=keyName,
    )

print(response)