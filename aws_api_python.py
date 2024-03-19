import boto3
import csv

dev=[{'Name': 'tag:env', 'Values': ['dev']}]
qa=[{'Name': 'tag:env', 'Values': ['qa']}]
prod=[{'Name': 'tag:env', 'Values': ['prod']}]

def list_aws_instances():
    _ec2 = boto3.client('ec2', region_name='us-east-1')

    resp = _ec2.describe_instances(Filters=dev)
    list_of_instances=[]
    for i in resp['Reservations']:
        for item in i['Instances']:
            #print("*********************************************")
            list_of_instances.append([(item['InstanceId'],item['ImageId'],item['InstanceType'],item['LaunchTime'],item['Placement']['AvailabilityZone'])])

            #print(item)

    return list_of_instances

with open("list_of_instance.csv", 'w',newline='') as f:  # 'w' , 'r', 'a'
   pen = csv.writer(f) 
   header = ["INSTANCE_ID", "IMAGE_ID" , "INSTANCE_TYPE", 'INSTANCE_LUNCH_TIME','AVAILABILITY_ZONE']
   pen.writerow(header)
   for a in list_aws_instances():
       pen.writerow(a)
f.close

