import boto3


client = boto3.client('ec2')

client.attach_volume(
    Device='/dev/data',
    InstanceId='i-0f0bf488d36714407',
    VolumeId='vol-086fb3afff955375a',
)
