import boto3
from io import BytesIO
from PIL import Image

client = boto3.client('s3')
source_bucket="media-app-initial-image"
destination_bucket="media-app-resized-image"
exclude_keys = {'cover/', 'post/', 'profile/'}

# Custom Image Size
cover_image_size = (820,360)
profile_image_size = (170,170)
post_image_size = (1080,1080)

def resizer(img, key):
    
    if key.startswith('cover'):
        resized_image = img.resize(cover_image_size)
    elif key.startswith('profile'):
        resized_image = img.resize(profile_image_size)
    elif key.startswith('post'):
        resized_image = img.resize(post_image_size)
        
    temp_buffer = BytesIO()
    resized_image.save(temp_buffer, format=img.format)
    resized_bytes = temp_buffer.getvalue()
    client.put_object(Body=resized_bytes, Bucket=destination_bucket, Key=key)


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
    
        with Image.open(BytesIO(image)) as img:
            img.format
            resizer(img,key)

