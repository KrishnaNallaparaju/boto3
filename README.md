# boto3
Following is the boto3 learning space and book keeping!

* boto3 is the name of the python module and very helpful now as the python SDK for aws!
*Open service
*it allows you to directy create, modify or delete the AWS resources from your Python scripts!

->  it's complicated in many ways but rich SDK for AWS

->  Boto3 is written on top of "botocore" which is a low level SDK for AWS - API.

-> Compare to botocore,  BOTO3 has a lot of useful methods to automate the AWS services.

*****  BOTOCORE is the basis for the AWS CLI which is also written in PYTHON

****************************************************************************************

INSTALL THE BOTO3 FOR YOUR SYSTEM!  In windows generally, by default BOTO3 will be installed by default when you install the Python

pip install boto3

With boto3 following collected packages will also be installed!

Installing collected packages: jmespath, urllib3, six, python-dateutil, botocore, s3transfer, boto3
Successfully installed boto3-1.16.30 botocore-1.19.30 jmespath-0.10.0 python-dateutil-2.8.1 s3transfer-0.3.3 six-1.15.0 urllib3-1.26.2

******************************************************************************************

CREDENTIALS MANAGEMENT:
----------------------

-> Directly with the service we can provide the AWS credentials during the resource object creation!

-> With above method the CREDENTIALS set will be exposed over the INTERNET during the public REPO's (if opted)

-> So, we can install awscli and configure the credentials which create the credentials file under "${HOME}/.aws/credentials" -  BOTO3 will pickup the credentials from here directly!

******************************************************************************************

CORE CONCEPTS OF BOTO3:
----------------------

-> resource				: high level object to access AWS services ( Creating objects / dot operations )
-> client               : low-level object to access AWS services ( Any manipulations to the existing object / dictonary operations )
-> meta     			: helps to enter into client object from resource object
-> session              : object to connect with particular AWS account or IAM user account and initiate a SESSION.
-> 


