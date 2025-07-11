import json, boto3, csv
s3 = boto3.client('s3')

def lambda_handler(event, context):a
    rec = event['Records'][0]['s3']
    src_bucket = rec['bucket']['name']
    src_key    = rec['object']['key']
    obj = s3.get_object(Bucket=src_bucket, Key=src_key)
    rows = csv.DictReader(obj['Body'].read().decode('utf-8').splitlines())

    enriched = []
    for row in rows:
        row['total_amount'] = float(row['quantity']) * float(row['price'])
        enriched.append(row)

    dest_key = src_key.replace('.csv', '.json')
    s3.put_object(Bucket='yourprefix-processed-orders', Key=dest_key, Body=json.dumps(enriched))
