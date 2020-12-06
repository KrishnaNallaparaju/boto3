#Python script for listing all the buckets from the AWS account

import boto3 #is the modules which holds the definitions of all the 

S3_obj = boto3.resource("s3")

#To list all the buckets from the AWS
for buckets in S3_obj.buckets.all():
    print(buckets.name)

