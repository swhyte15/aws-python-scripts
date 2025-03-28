import boto3

def upload_file(bucket_name, file_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    s3.upload_file(file_name, bucket_name, object_name)

# Example usage
# upload_file('my-bucket', 'test.txt')
