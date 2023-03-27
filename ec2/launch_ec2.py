import boto3

# Set up the boto3 client
region = 'ap-northeast-1'
client = boto3.client('ec2', region_name=region)

# Define the instance configuration parameters
image_id = 'ami-0086c8dbddc8963e9'
instance_type = 't2.micro'
key_name = 'aws_access'

# Create the instance
response = client.run_instances(
    ImageId=image_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {   
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Boto3-demo'
                },
            ]
        },
    ],
)


# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Instance created with ID: {instance_id}')
