from sg import *
from getImage import *
from createKey import *
# from createVolumes import *
import yaml
import boto3
from sys import argv
import pdb

# Read yaml file
def readFile(filename):
    try:
        with open(filename, "rt") as f:
            data = yaml.safe_load(f)
        return data
    except:
        print("File by that name doesn't exist.")

# Build the instance
def buildInfra(config, ami, sg, key):

    user_data = '''#!/bin/bash
        sudo useradd -p user1pw user1
        sudo useradd -p user1pw user2
        sudo echo 'AllowUsers user1 user2 ec2-user' >> /etc/ssh/sshd_config
        sudo echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
        sudo restart ssh
        sudo mkdir /data
        sudo mkfs -t {} /dev/xvdf
        sudo mount -t xfs /dev/xvdf /data
        sudo chmod ugo+rwx /data
        sudo mkdir /home/{}/.ssh
        sudo mkdir /home/{}/.ssh
        sudo touch /home/{}/.ssh/authorized_keys
        sudo touch /home/{}/.ssh/authorized_keys
        sudo echo '{}' >> /home/{}/.ssh/authorized_keys
        sudo echo '{}' >> /home/{}/.ssh/authorized_keys
        '''.format(config['server']['volumes'][1]['type'],
                config['server']['users'][0]['login'],
                config['server']['users'][1]['login'],
                config['server']['users'][0]['login'],
                config['server']['users'][1]['login'],
                config['server']['users'][0]['ssh_key'],
                config['server']['users'][0]['login'],
                config['server']['users'][1]['ssh_key'],
                config['server']['users'][1]['login'])
        #         sudo systemctl restart sshd
    client = boto3.resource('ec2')
    instance = client.create_instances(
        ImageId=ami['ImageId'],
        InstanceType=config['server']['instance_type'],
        MinCount=config['server']['min_count'],
        MaxCount=config['server']['max_count'],
        SecurityGroupIds=[sg['GroupId']],
        KeyName = key['KeyName'],
        UserData = user_data,

        BlockDeviceMappings=[
            {
                'DeviceName': config['server']['volumes'][0]['device'],
                # 'VirtualName': 'string',
                'Ebs': {
                    'DeleteOnTermination': True,
                    # 'Iops': 123,
                    # 'SnapshotId': 'string',
                    'VolumeSize': config['server']['volumes'][0]['size_gb'],
                    'VolumeType': 'gp2',
                    # 'KmsKeyId': 'string',
                    # 'Throughput': 123,
                    # 'OutpostArn': 'string',
                    'Encrypted': False
                },
                # 'NoDevice': 'string'
            },
            {
                'DeviceName': config['server']['volumes'][1]['device'],
                # 'VirtualName': 'string',
                'Ebs': {
                    'DeleteOnTermination': True,
                    # 'Iops': 123,
                    # 'SnapshotId': 'string',
                    'VolumeSize': config['server']['volumes'][1]['size_gb'],
                    'VolumeType': 'gp2',
                    # 'KmsKeyId': 'string',
                    # 'Throughput': 123,
                    # 'OutpostArn': 'string',
                    'Encrypted': False
                },
                # 'NoDevice': 'string'
            },
        ],
    )



script, yamlFile = argv

config = readFile(yamlFile)
ami = getImageId(config)
sg = buildSG()
key = createKey()

buildInfra(config, ami, sg, key)

# print(sg)
# print("conf", config['server']['ami_type'] +'*')
