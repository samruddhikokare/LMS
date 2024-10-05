import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = 'your_aws_access_key_id'
AWS_SECRET_ACCESS_KEY = 'your_aws_secret_access_key'
AWS_STORAGE_BUCKET_NAME = 'your_s3_bucket_name'
AWS_S3_REGION_NAME = 'your_region_name'  # e.g., 'us-east-1'

def create_s3_client():
    """Create and return an S3 client."""
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_S3_REGION_NAME
        )
        return s3_client
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error creating S3 client: {e}")
