import boto3
import PIL 
client = boto3.client('s3')

fileName='files/test.txt'
bucketName = "media-app-resized-image"
keyName ="files/test.txt"


response = client.upload_file(
    fileName,
    bucketName, 
    keyName,
)

print(response)