import json
import boto3

def lambda_handler(event, context):
    try:
        runtime = boto3.client('sagemaker-runtime')
        endpoint = 'huggingface-pytorch-inference-2024-12-07-18-39-56-639'
        text = event['body']
        print('This is the text to be summarized: ', text)

        response = runtime.invoke_endpoint(
                EndpointName=endpoint,
                ContentType='application/json',
                Body=json.dumps({"inputs": text})
        )

        summary = json.loads(response['Body'].read().decode())

        print('Summary: ', summary)

        return {
            'statusCode': 200,
            'body': json.dumps(summary[0]['summary_text'])
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
