import boto3

bucketName = "mytestbuckte1054589"
keyName ="Interview.docx"

client = boto3.client('s3')

response = client.delete_object(
    Bucket=bucketName,
    Key=keyName,
)

print(response)