import boto3

def list_ec2_instances(region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'State': instance['State']['Name'],
                'Type': instance['InstanceType'],
                'LaunchTime': instance['LaunchTime'].isoformat()
            })
    return instances
