import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = event.get('instanceId')
    if not instance_id:
        return {"statusCode": 400, "body": "Missing instanceId"}

    try:
        ec2.reboot_instances(InstanceIds=[instance_id])
        return {"statusCode": 200, "body": f"Instance {instance_id} rebooted successfully."}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}