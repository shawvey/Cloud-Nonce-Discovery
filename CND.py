import boto3
import time
import sys
import datetime
import os
from fabric.api import *


env.user = 'ubuntu'
env.key_filename = '~/.ssh/ec2_comsm0010.pem'


@serial
def StartInstances(N):
	#Create N instances
	ec2=boto3.client('ec2',region_name='us-east-1')
	ubuntu_id='ami-04b9e92b5572fa0d1'
	type='t2.micro'

	key_pair='ec2_comsm0010'
	Response=ec2.run_instances(ImageId=ubuntu_id,InstanceType=type,KeyName=key_pair,SecurityGroups=['launch-wizard-16'],MinCount=int(N),MaxCount=int(N))
	#Wait for running of our instances
	time.sleep(100)
	filters = [{ 'Name': 'instance-state-name', 'Values': ['running']}]
	Reservations=ec2.describe_instances(Filters=filters)
	# Get the public ip address of all instances
	MyHosts = []
	for r in Reservations['Reservations']:
		for instance in r['Instances']:
			MyHosts.append(instance['PublicIpAddress'])
	return MyHosts


@parallel
def RunInstances(T,D,N,ihosts):
	sqs = boto3.client('sqs')
	response=sqs.get_queue_url(QueueName='CloudComputing')
	#upload PoW to each VM
	put('PoW.py', 'PoW.py', use_sudo=True)

	#Get the instance number
	for num in range(int(N)):
		if env.host == ihosts[num]:
			LowRange = num
	start_time = datetime.datetime.now()
	#step
	for CurrentNum in range(int(LowRange),2**32,int(N)):
		Getvalue = run("python3 -c 'import PoW;PoW.goldennonce(%d,%s)'"%(int(D),str(CurrentNum)))
		end_time = datetime.datetime.now()
		interval = (end_time-start_time).total_seconds()
		#if get value,send a message to the queue
		if Getvalue != '':
			print('total runtime is %f seconds!'%float(interval))
			sqs.send_message(QueueUrl=response['QueueUrl'],MessageBody='Finished!')
			break
		if float(interval) >= float(T):
			print('Timeout!')
			break
		#check whether one instance finishs or not
		response=sqs.get_queue_url(QueueName='CloudComputing')
		messages = sqs.receive_message(QueueUrl=response['QueueUrl'])
		if 'Messages' in messages:
			break
	# download log files into our local machine
	get('/var/log/syslog','logs/Instance%d.log'%int(LowRange), use_sudo=True)

 
def start(T,D,N):
	# Create SQS queue
	sqs = boto3.client('sqs')
	response = sqs.create_queue(
    	QueueName='CloudComputing',
	)
	MyHosts = StartInstances(N)
	execute(RunInstances,T,D,N,MyHosts,hosts = MyHosts)
	# Delete SQS queue
	sqs.delete_queue(QueueUrl=response['QueueUrl'])
	Scram()
	upload_logs()


def Scram():
	# Terminate all running instances
	ec2=boto3.client('ec2',region_name='us-east-1')
	filters = [{ 'Name':'instance-state-name','Values': ['running']}]
	Reservations=ec2.describe_instances(Filters=filters)
	for r in Reservations['Reservations']:
		for instance in r['Instances']:
			n=instance['InstanceId']
			ec2.terminate_instances(InstanceIds=[n])

def upload_logs():
	# upload log files to our s3
    s3_resource = boto3.resource("s3", region_name="us-east-1")
    try:
        bucket_name = "cloudcomputinglogs" #s3 bucket name
        root_path = './logs' # local folder for upload

        my_bucket = s3_resource.Bucket(bucket_name)

        for path, subdirs, files in os.walk(root_path):
            directory_name = path.replace(root_path,"logs")
            for file in files:
                my_bucket.upload_file(os.path.join(path, file), directory_name+'/'+file)

    except Exception as err:
        print(err)

