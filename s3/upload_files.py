import boto3

client = boto3.client('s3')

fileName='files/test.txt'
bucketName = "mytestbuckte1054589"
keyName ="test.txt"


response = client.upload_file(
    fileName,
    bucketName, 
    keyName,
)

print(response)