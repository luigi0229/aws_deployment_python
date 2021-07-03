# import boto3
#
# def createVolumes(config):
#     client = boto3.client('ec2')
#     response = client.create_volume(
#         AvailabilityZone='us-east-1a',
#         Encrypted=False,
#         #Iops=100,
#         #KmsKeyId='string',
#         Size=10,
#         #SnapshotId='string',
#         VolumeType='gp2',    #standard'|'io1'|'gp2'|'sc1'|'st1',
#         DryRun=False,
#     )
#
#     response2 = client.create_volume(
#         AvailabilityZone='us-east-1a',
#         Encrypted=False,
#         #Iops=100,
#         #KmsKeyId='string',
#         Size=100,
#         #SnapshotId='string',
#         VolumeType='gp2',    #standard'|'io1'|'gp2'|'sc1'|'st1',
#         DryRun=False,
#     )
#
#     # print("volss", response)
#     volIds = [response['VolumeId'], response2['VolumeId']]
#
#     return(volIds)
