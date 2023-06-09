import boto3

s3_client = boto3.client('s3',
                         region_name='us-east-1',
                         aws_access_key_id='AKIAZQXFZ46H2DGAUV5D',
                         aws_secret_access_key="taUlMb47wAFGv0z+b61o8bwFcyCnft1MCdP0jbdR"
                         )

s3_client.put_object(Bucket='denny-example-bucket', Key="test.txt", Body=b"this is a test", ServerSideEncryption='aws:kms')
