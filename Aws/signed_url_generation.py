import boto3
from botocore.exceptions import NoCredentialsError
from botocore.signers import CloudFrontSigner
import rsa
import datetime

def generate_presigned_url(bucket_name, object_key, expiration=3600):
    """
    Generate a presigned URL for an S3 object.

    :param bucket_name: Name of the S3 bucket
    :param object_key: Key of the S3 object
    :param expiration: Expiration time in seconds (default is 3600 seconds)
    :return: Presigned URL as a string
    """
    s3_client = boto3.client('s3')

    try:
        response = s3_client.generate_presigned_url('get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=expiration
        )
    except NoCredentialsError:
        print("Credentials not available")
        return None

    return response

def generate_cloudfront_signed_url(cloudfront_url, private_key_file, key_id, expiration_time):
    """
    Generate a signed URL for a CloudFront distribution.

    :param cloudfront_url: The CloudFront URL for the S3 object
    :param private_key_file: Path to the private key file
    :param key_id: CloudFront key pair ID
    :param expiration_time: Expiration time as a datetime object
    :return: Signed URL as a string
    """
    with open(private_key_file, 'rb') as key_file:
        private_key = key_file.read()

    signer = CloudFrontSigner(key_id, lambda message: rsa.sign(message.encode('utf-8'), private_key, 'SHA-1'))

    signed_url = signer.generate_signed_url(
        cloudfront_url,
        date_less_than=expiration_time
    )

    return signed_url

# Example Usage
if __name__ == "__main__":
    # Presigned URL example
    bucket_name = 'your_bucket_name'
    object_key = 'path/to/your/video.mp4'
    
    presigned_url = generate_presigned_url(bucket_name, object_key)
    print("Presigned URL:", presigned_url)

    # CloudFront signed URL example
    cloudfront_url = 'https://your_distribution.cloudfront.net/path/to/your/video.mp4'
    private_key_file = 'path/to/your/private_key.pem'
    key_id = 'your_key_id'
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    signed_cloudfront_url = generate_cloudfront_signed_url(cloudfront_url, private_key_file, key_id, expiration_time)
    print("CloudFront Signed URL:", signed_cloudfront_url)
