'''
Programmer : Krishna Nallaparaju
Date       : 07/12/2020
Details    : To list the ec2 instances in a console format
Language   : Python
'''

#Import all the required modules!
import boto3   #acts as browser to access AWS resources

#Function definitions
#def prCyan(a, b): print("\033[96m {}\033[00m" .format(a * b))
def line_sep(string, times): print(string * times)
def string_ljust(string1,string2,string3,string4,string5,string6,length): print("|{}|{}|{}|{}|{}|{}|". format(string1.ljust(length, ' '),string2.ljust(length, ' '),string3.ljust(length, ' '),string4.ljust(length, ' '),string5.ljust(length, ' '),string6.ljust(length, ' ')))

#SESSION OBJECT CREATION 
session_obj = boto3.Session(profile_name="default", region_name=input("Please enter your region to list ec2 instance details:"))
#session_obj = boto3.Session(profile_name="default", region_name="us-east-1")

#Client OBJECT FOR 'ec2'
ec2_obj = session_obj.resource('ec2')   # // Currently using "resource" for gathering highlevel info, we can use "client" for indepth actions!

line_sep('-',203)
string_ljust('Name','Instance ID','Instance state','Instance type','VPC ID','Launch time',33)
line_sep('-',203)

for instance in ec2_obj.instances.all():
    String1=instance.tags[0]['Value']
    String2=instance.id
    String3=instance.state['Name']
    String4=instance.instance_type
    String5=instance.vpc_id
    String6=str(instance.launch_time)
    string_ljust(String1,String2,String3,String4,String5,String6,33)
    line_sep('-',203)