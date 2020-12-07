import boto3

#Set the Session object!
sess_obj=boto3.Session(profile_name='cloud-user', region_name='us-east-1')

res_obj=sess_obj.resource('ec2')

for instance in res_obj.instances.all():
    print(instance.id)

