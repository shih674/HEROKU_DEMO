import boto3
# 創造S3的客戶端
s3Client = boto3.client('s3', aws_access_key_id='AKIAR4NDUH53GWDLQFNM', aws_secret_access_key='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')

# 用客戶端上傳圖片到S3 bucket內，iii-tutorial-v2
#s3Client.upload_file(file_name, bucket, object_name)
s3Client.upload_file('Procfile', 'iii-tutorial-v2', 'student28/Procfile')