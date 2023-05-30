import boto3
import base64

rekognition = boto3.client('rekognition', 'ap-northeast-2')

# [이미지 파일 경로] 예시=> '/content/drive/MyDrive/000bec180eb18c7604dcecc8fe0dba07.jpg'
with open([이미지 파일 경로], "rb") as cf:
    base64_image=base64.b64encode(cf.read())
    base_64_binary = base64.decodebytes(base64_image)
    print("file open!")

    response = rekognition.detect_labels(Image={'Bytes': base_64_binary})
    response
