import json
import boto3
from boto3.dynamodb.conditions import Attr

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('MutantsDBTable')
def lambda_handler(event, context):

    mutants=table.scan(
        Select='COUNT',
        FilterExpression=Attr('isMutant').eq(1)
        )

    humans=table.scan(
        Select='COUNT',
        FilterExpression=Attr('isMutant').eq(0)
        )

    ratio=mutants['Count']/humans['Count']
    print(ratio,mutants['Count'],humans['Count'])
    return {
        "statusCode": 200,
        "body": json.dumps({
            "count_mutant_dna": mutants['Count'],
            "count_human_dna": humans['Count'],
            "ratio":ratio
        }),
    }
