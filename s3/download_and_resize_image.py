import boto3
from io import BytesIO
from PIL import Image

client = boto3.client('s3')
source_bucket="media-app-initial-image"
destination_bucket="media-app-resized-image"
exclude_keys = {'cover/', 'post/', 'profile/'}
profile_image_size = (170,170)
cover_image_size = (820,360)
post_image_size = (1080,1080)

def profile_resize(image, key):
    image.resize(profile_image_size)
    resized_image = image.tobytes()
    #client.put_object(Body=resized_image, Bucket=destination_bucket, Key=key)
    #image.save('profile_image2.png')
    client.put_object(Body=resized_image, Bucket=destination_bucket, Key=key)

def download_image(bucketName,key):
    image_object = client.get_object(Bucket=bucketName,Key=key)
    image_content = image_object['Body'].read()
    return image_content

response = client.list_objects_v2(Bucket=source_bucket)
for item in response['Contents']:
    key = item['Key']
    if key not in exclude_keys:
        print(item['Key'])
        image = download_image(source_bucket,key)
        #print(image)
        
        with Image.open(BytesIO(image)) as img:
            #img.show()
            img.format
            profile_resize(img,key)


