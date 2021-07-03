import boto3

def createKey():
        ec2 = boto3.client('ec2')
        response = ec2.create_key_pair(KeyName='k1')
        # f = open("k1.pub", "a")
        # f.write(response['KeyMaterial'])
        # f.close()

        f2 = open("k1.pem", "a")
        f2.write(response['KeyMaterial'])
        f2.close()

        return(response)
