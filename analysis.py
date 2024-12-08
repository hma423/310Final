import json

import os, boto3

client = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        if "body" not in event:
            return {
                'statusCode': 500,
                'body': json.dumps("There must be a body of text included!")
            }
            
        print("this is the entire event: ", event)
        print("this is the input: ", event['body'])
        ourText = event["body"]
        result = client.detect_sentiment(Text=ourText, LanguageCode='en')
        print(result)
        result = result['Sentiment']
        print("hello my name is bob")
        print(result)
        return {
            'statusCode': 200,
            'body': json.dumps({'Sentiment': result})
        }
    

    except Exception as e:
        print("we got an error here: ", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }