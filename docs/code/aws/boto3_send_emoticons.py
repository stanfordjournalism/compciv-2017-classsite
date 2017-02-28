import boto3
# https://boto3.readthedocs.io/en/latest/reference/services/ses.html#SES.Client.send_email

session = boto3.Session(profile_name='default')
ses = session.client('ses')


from_addr = 'YOUR_ADDRESS@stanford.edu'
# let's CC ourselves at least
destination = {'ToAddresses': ['TARGET_ADDRESS@stanford.edu'],
                'CcAddresses': [from_addr]}

subject_line = "hey what is up d00d? ;)"

bodytext = """
Dear d00d,

How do you like them emoji?

😈 👿 👹 👺 💩 👻

💀 ☠️ 👽 👾 🤖 🎃

😺 😸 😹 😻 😼 😽

- Me <3
"""



msg = {
        "Subject": {
            "Charset": "utf8",
            "Data": subject_line
        },
        "Body": {
            "Text": {
                "Charset": "utf8",
                "Data": bodytext
            }
        }
    }



ses.send_email(Source=from_addr, Destination=destination, Message=msg)


