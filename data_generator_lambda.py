import json
import boto3

s3_client = boto3.client('s3')


def lambda_handler(event, context):
    fitered_record = event[0]
    airbnb_record = fitered_record['body']
    message_id = fitered_record['messageId']

    # print("Body:", body)
    # print("MessageId:", message_id)
    
    bucket_name = 'airbnb-booking-records-vyas'
    file_name = f"{fitered_record['messageId']}.json"  # Using messageId as file name
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(airbnb_record)
    )
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Record is saved successfully!')
    }
