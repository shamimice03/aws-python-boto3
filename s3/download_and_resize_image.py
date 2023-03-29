import boto3
from io import BytesIO
from PIL import Image

client = boto3.client('s3')
source_bucket = "media-app-initial-image"
destination_bucket = "media-app-resized-image"
exclude_keys = {'cover/', 'post/', 'profile/'}

# Custom Image Size
image_sizes = {
    'cover': (820, 360),
    'profile': (170, 170),
    'post': (1080, 1080)
}

def resizer(img, key):
    image_type = key.split("/")[0]
    if image_type in image_sizes:
        resized_image = img.resize(image_sizes[image_type])
        temp_buffer = BytesIO()
        resized_image.save(temp_buffer, format=img.format)
        resized_bytes = temp_buffer.getvalue()
        client.put_object(Body=resized_bytes, Bucket=destination_bucket, Key=key)


def download_image(bucket_name, key):
    response = client.get_object(Bucket=bucket_name, Key=key)
    return response['Body'].read()


response = client.list_objects_v2(Bucket=source_bucket)
for item in response['Contents']:
    key = item['Key']
    if key not in exclude_keys:
        print(key)
        image_content = download_image(source_bucket, key)
        with Image.open(BytesIO(image_content)) as img:
            img.format
            resizer(img, key)

# Add Layer to Lambda
# Ref: https://repost.aws/knowledge-center/lambda-import-module-error-python
 # Install python3.9 first
 # python3.9 -m pip install Pillow -t python/
 # zip -r layer.zip python
 # aws lambda publish-layer-version --layer-name pli-layer --zip-file fileb://layer.zip --compatible-runtimes python3.9 --region ap-northeast-1
