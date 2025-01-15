import boto3
import os
import git

# Initialize S3 client
s3 = boto3.client('s3')

# Path to the directory containing the non-code assets
assets_dir = '/path/to/non-code-assets/'

# Sync assets to S3
def sync_assets_to_s3(bucket_name):
    for root, dirs, files in os.walk(assets_dir):
        for file in files:
            file_path = os.path.join(root, file)
            s3.upload_file(file_path, bucket_name, file)
            print(f"Uploaded {file_path} to S3")

# Sync the assets to the S3 bucket
sync_assets_to_s3('your-s3-bucket-name')
