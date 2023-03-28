import json
import boto3


with open("files/event.json") as js:
    event = json.load(js)
    print(event)

for item in event['Records']:
    print(f"item-{item['body']}")
    for each in item['body']['Records']:
        print(f"bucketName: {each['s3']['bucket']['name']}")
        print(f"objectKey: {each['s3']['object']['key']}")
        
        


# Test Event

# {
#   "Records":[
#       {
#          "messageId":"7ab272a5-4a8f-4f2d-862b-4bc788c223d7",
#          "receiptHandle":"AQEBGsotsG/HTVbeBeKsfMhWb6O3BBqYmF35uFq1yW01z39+XMPiYxqJrfn+6o2EAks3XT5+Knpg/5VGBf0WLqVnbRxq/JT9Fo0tfP+UWFsGrsgQTWyPYssM8SN2Vy1PTJ0pk/lcr//O43aEC/86A9EC2QR8HUlLrImTMKTtexU9nM0WjAvRL0BpLcZcpj7KEynyKLeQJ0kcBf2iI/K+cHsAzA4c2st5bDRv8XUjDMzyFwpICk+7Xxz1PqvLywe6Zhrk+157s5X3eWlGoU1V9J79/O/i8Yyferp69wAynmTl5gRxlqpCmhPNeaSs/n5docRL5MCXj/HVLfzCntacheNPeCM8h3OGyD9dogNGyKrbv/0xWadjkIcu4/X4OACGbWmOwQNBKYeeJKLIeEHRqzgOWA==",
#          "body":"{\"Service\":\"Amazon S3\",\"Event\":\"s3:TestEvent\",\"Time\":\"2023-03-28T01:46:41.286Z\",\"Bucket\":\"media-app-initial-image\",\"RequestId\":\"DYHW54A6WNTKN4NM\",\"HostId\":\"rOsGNfIZovn1aAzQ/5Tl2rWxL7cwaza8j+b7osNF1Kn80Ye0V17M22vm08OXkGsBuibpqu9YZvA=\"}",
#          "attributes":{
#             "ApproximateReceiveCount":"5",
#             "SentTimestamp":"1679968001314",
#             "SenderId":"AIDAJLLOM6JFFZDEDBYEG",
#             "ApproximateFirstReceiveTimestamp":"1679984094869"
#          },
#          "messageAttributes":{
            
#          },
#          "md5OfMessageAttributes":"None",
#          "md5OfBody":"4814a8378c8ce50486d6b547ad59848a",
#          "eventSource":"aws:sqs",
#          "eventSourceARN":"arn:aws:sqs:ap-northeast-1:391178969547:media-app-queue",
#          "awsRegion":"ap-northeast-1"
#       }
#   ]
# }

# def lambda_handler(event, context):
#     # TODO implement
#     print(event)
#     try:
#         for i in event['Records']:
#             s3_event = json.loads(i['body'])
#             if 'Event' in s3_event and s3_event['Event'] == 's3:TestEvent':
#                 print("Test Event")
#             else:
#                 for j in s3_event['Records']:
#                     print("Bucket Name : {} ".format(j['s3']['bucket']['name']))
#                     print("Object Name : {} ".format(j['s3']['object']['key']))
#     except Exception as exception:
#         print(exception)