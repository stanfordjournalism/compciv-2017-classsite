import boto3

ses = boto3.client('ses')


from_field = 'dan@danwin.com'
dest_field = {'ToAddresses': ['dun@stanford.edu']}
msg = {'Subject': {'Data': 'hey there', 'Charset': 'utf8'},
        'Body': {'Text': {'Data': 'Hello', 'Charset': 'utf8'}}}


ses.send_email(Source=from_field, Destination=dest_field, Message=msg)


rsname = "CompcivMadeMeDoThis"
ses.create_receipt_rule_set(RuleSetName=rsname)
ses.create_receipt_rule(RuleSetName=rsname,
        Rule={'Name': 'whatever', 'Enabled': True})
