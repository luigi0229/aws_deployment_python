import boto3

# Fetch a list of images based on the yaml's file info
# Sort the list of images and return first (latest created) element

def getImageId(config):
    client = boto3.client('ec2')
    response = client.describe_images(
        Owners=['amazon'],
        Filters=[ {
                'Name': 'name',
                'Values': [config['server']['ami_type']+'*']
            },
            # {
            #     'Name': 'description',
            #     'Values': ['Amazon Linux 2 AMI 2.0.2021*']
            # },
            {
                'Name': 'architecture',
                'Values': [config['server']['architecture']]
            },{
                'Name': 'state',
                'Values': ['available']
            },{
                'Name': 'root-device-type',
                'Values': [config['server']['root_device_type']]
            },{
                'Name': 'virtualization-type',
                'Values': [config['server']['virtualization_type']]
            },{
                'Name': 'image-type',
                'Values': ['machine']
            }],

    )
    response['Images'].sort(key=lambda x: x['CreationDate'], reverse=True)
    # pdb.set_trace()
    try:
        return(response['Images'][0])
    except:
        print("Could not find a valid image")
