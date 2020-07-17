# 引用套件
import boto3

#一些參數
file_name = 'ngrok_is_shit.txt'
bucket = 'iii-tutorial-v2'
object_name = 'student28/ngrok_is_shit.txt'

# 上傳檔案到S3
# upload file to s3 boto3


# 創建客戶端
s3_client = boto3.client('s3')

# 用客戶端上傳到S3的Bucket
response = s3_client.upload_file(file_name, bucket, object_name)

#印出結果
print(response)

# 用戶從S3下載檔案
s3_client.download_file(bucket, object_name, '0701.txt')
print(response)