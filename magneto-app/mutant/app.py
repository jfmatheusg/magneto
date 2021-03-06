import json
import numpy as np
import boto3
from Crypto.Hash import SHA256

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('MutantsDBTable')

def checkDna(dnaStrip):
    mutantChains = ["AAAA","CCCC","GGGG","TTTT"]
    mutationsCount=0
    for mutantChain in mutantChains:
        if mutantChain in dnaStrip:
            mutationsCount+=dnaStrip.count(mutantChain)
            if mutationsCount>1:
                break

    return mutationsCount

def isMutant(dna):

    mutations = 0
    for dnaRow in dna:
        mutations+= checkDna(dnaRow)
        if mutations>1:
            return True

    dnaMatrix = np.array([list(row.encode()) for row in dna])

    dnaMatrixT = dnaMatrix.T
    for column in dnaMatrixT:
        dnaColumn = bytes(column.tolist()).decode()
        mutations+= checkDna(dnaColumn)
        if mutations>1:
            return True

    dnaMatrixF = np.fliplr(dnaMatrix)
    lenRow=len(dna)
    for offset in range(-lenRow+4,lenRow-3):
        dnaDiagonal = bytes(np.diagonal(dnaMatrix,offset).tolist()).decode()
        dnaDiagonalF = bytes(np.diagonal(dnaMatrixF,offset).tolist()).decode()
        mutations+= checkDna(dnaDiagonal + " " + dnaDiagonalF)
        if mutations>1:
            return True
    return False


def lambda_handler(event, context):
    body = json.loads(event['body'])
    dna = body['dna']
    mutant = isMutant(dna)
    hash = SHA256.new()
    hash.update(("".join(dna)).encode('utf-8'))
    dnaKey=hash.hexdigest()
    table.put_item(
        Item={
            "dna": dnaKey,
            "isMutant": 1 if mutant else 0
            })
    if mutant:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Mutant!",
            }),
        }
    else:
        return {
            "statusCode": 403,
            "body": json.dumps({
                "message": "Forbidden",
            }),
        }
