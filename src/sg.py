import boto3

# Create Security Group and allow SSH in
def buildSG():
    ec2 = boto3.client('ec2')
    sg = ec2.create_security_group(
        Description='Allow SSH',
        GroupName='allow_ssh_in',
    )

    ec2.authorize_security_group_ingress(
        GroupId=sg['GroupId'],
        CidrIp='0.0.0.0/0',
        IpProtocol='tcp',
        FromPort=22,
        ToPort=22
        )
    return(sg)
