# AWS Instance Deployment using Python and Boto3

ONLY TESTED ON PYTHON 2.7 SO FAR!

This repository contains the required python code to
deploy an AWS EC2 instance using Python and Boto3.
The code is designed to read from a YAML configuration file that
should be passed as a parameter when running the main module, and the
deployment will use the yaml configuration to deploy the environment.

## Pre-requisites

  * Valid YAML template like the one in the src folder. Two Volumes and Two users required.
  Min_count and Max_count parameters are currently being ignored.

  * Resources with the same names/tages cannot already exist on the AWS Deployment region.
   If there is a group that has the same name as the one created in the deployment (`allow_ssh_in`) or a keypair (`k1`) the deployment will fail.

  * AWS CDK environment configured and initialized with required credentials

  * Python installed, with required dependencies. Run `pip install -r requirements.txt` on the root of the src file to install required libraries.

  * A key that will be used for SSH for each of the two
  users on the configuration. To create a new key on an Unix environment, use command `ssh-keygen -f keyname.pem` where keyname.pem is the name of your key. Follow the prompts. Paste the public key of each user on it's associated key on
  the YAML file (ssh_key)
  THE PUBLIC KEY ON THE YAML NEEDS TO 100% MATCH THE ORIGINAL.

  * The first EBS Volume that gets created will hold the OS. Make sure the size is big enough so that the AMI snapshot could fit. Made the size 50GBs for now.


## Deployment

    python main.py deployment.yaml

## Post Deployment

  Post deployment, the instance will be created, along with a keypair by the name of `k1.pem` that can be used with defult instance's user (ec2-user for specific AMIs) to ssh in.

  You should be able to SSH in either using the k1.pem key with ec2-user, or either of the users on the YAML file and their corresponding private key. The required security group that allows SSH in is automatically created.

  Both users will have Read/Write access to the EBS mounted on /data, but they will not have access to the OS mount /. They only have Read/Write access on this mount under their corresponding home directories.

## Troubleshooting

  Manually delete already created resources everytime if you want to run the script multime times. If something fails on the deployment and you need to run it again, make sure that:
    * `k1.pem` file doesn't exist in current directory
    * `k1` keypair doesn't exist on AWS.
    * `allow_ssh_in` security group doesn't exist. 
