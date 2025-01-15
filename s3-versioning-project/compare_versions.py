import boto3

# Initialize S3 client
s3 = boto3.client('s3')

def list_versions(bucket_name, file_name):
    versions = s3.list_object_versions(Bucket=bucket_name, Prefix=file_name)
    for version in versions['Versions']:
        print(f"VersionId: {version['VersionId']} - LastModified: {version['LastModified']}")

# List versions of a specific file
list_versions('your-s3-bucket-name', 'config.yaml')
