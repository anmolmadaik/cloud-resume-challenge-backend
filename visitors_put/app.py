import json
import boto3
import traceback


client = boto3.client('dynamodb')

def lambda_handler(event, context):
   
    try:

        print(event)
        print('deployed')

        if event["requestContext"]["http"]["method"] == "OPTIONS":
            return {"statusCode": 200}

        body = json.loads(event['body'])
        value = body['value']

        client.update_item(
            TableName = 'visitors',
            Key = {
                'id': {
                    "N": "1"
                }
            },
            UpdateExpression = "SET count_visitors = :s",
            ExpressionAttributeValues = {
                ':s': {
                    "N": str(value)
                }
            }

        )

        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': "Updated successfully"})
        }

    except Exception as e:
        print(traceback.format_exc())
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': 'http://127.0.0.1:3000,https://resume.anmolmadaik.com',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': "An exception occured", "exception": str(e)})
        }

