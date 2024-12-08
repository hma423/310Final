import json

import os, boto3


client = boto3.client('translate')


def lambda_handler(event, context):
    try:
        print("thisis the event: ", event)
        print(event['pathParameters'])
        if 'body' not in event or 'language' not in event['pathParameters']:
            return{
                "statusCode" :500,
                "body": json.dumps("Something missing from api call")
            }
        targetLanguage = event['pathParameters']['language']
        
        if not targetLanguage or targetLanguage == "":
            return{
                "statusCode" :500,
                "body": json.dumps("empty target language")
            }

        print("this is the target langauge our users inputted: ", targetLanguage)

        #checking if input langauge exists
        languageCodes = client.list_languages()

        storedLanguageCodes = set()
        
        for i in languageCodes['Languages']:
            storedLanguageCodes.add(i['LanguageCode'])

        if targetLanguage not in storedLanguageCodes:

            return {
                "statusCode" : 500,
                "body" : json.dumps("Error with Language Code")
            }

        print("this is our body text: ", event['body'])
        inputText = event['body']
        print(inputText)
        response = client.translate_text(
            Text = inputText,
            SourceLanguageCode='en',
            TargetLanguageCode=targetLanguage,
        )
        print("this is th response: ", response['TranslatedText'])
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }

    except Exception as e:
        print("in the exception area")
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
