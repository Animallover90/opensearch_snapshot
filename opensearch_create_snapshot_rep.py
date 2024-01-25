import boto3
import requests
from requests_aws4auth import AWS4Auth

bucket = "생성하고자 하는 bucket명"
role_arn = "만들었던 Role의 arn"
host = "https://search-test-opensearch-본인의 OpenSearch 엔드포인트.es.amazonaws.com"
region = "ap-northeast-2"
service = "es"

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

# Register snapshot repository

path = "/_snapshot/" + bucket
url = host + path

payload = {
    "type": "s3",
    "settings": {
        "bucket": bucket,
        "base_path": "backup/",
        "region": region,
        "role_arn": role_arn
    }
}

headers = {"Content-Type": "application/json"}

r = requests.put(url, auth=awsauth, json=payload, headers=headers)

print(r.status_code)
print(r.text)