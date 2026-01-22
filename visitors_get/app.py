import json
import boto3


client = boto3.client('dynamodb')

def lambda_handler(event, context):
   
    try:

        item = client.get_item(
            TableName='visitors',
            Key={
                'id': {
                    'N': '1'
                }
            },
            ProjectionExpression='count_visitors'
        )
        result = int(item.get('Item').get('count_visitors').get('N'))

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': 'http://127.0.0.1:3000,https://resume.anmolmadaik.com',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Content-Type': 'application/json'
            },
            'body': json.dumps(result)
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({"message": "An exception occured",'error': str(e)})
        }

