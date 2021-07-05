# AWS Instance Deployment using Python and Boto3

This repository contains the required python code to
deploy an AWS EC2 instance using Python and Boto3.
The code is designed to read from a YAML configuration file that
should be passed as a parameter when running the main module, and the
deployment will use the yaml configuration to deploy the environment.

## prerequisites

  * AWS CDK environment configured and initialized with required credentials

  * Python installed, with required dependencies

  * Create an key that will be used for SSH for each of the two
  users on the configuration. To create a new key, use command below:

      ssh-keygen -f keyname

  * Follow the prompts. This will generate a new key with name
  'keyname' and a corresponding public key 'keyname.pub'
  Paste the public key of each user on it's associated key on
  the YAML file (ssh_key)
  THE PUBLIC KEY ON THE YAML NEEDS TO 100% MATCH THE ORIGINAL.
  DO NOT INCLUDE THE user1@localhost THAT IS WAS PRE-CONFIGURED ON THE YAML FILE.



## Deployment

    pip3install requirements.txt

    python main.py deployment.yaml
