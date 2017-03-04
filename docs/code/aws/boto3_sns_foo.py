# https://boto3.readthedocs.io/en/latest/reference/services/sns.html#client

import boto3

# phonenum='+1555555555'

# sns = boto3.client('sns')
# sns.publish(PhoneNumber=phonenum,
#     Message='Simple text message')

MSG_TEMPLATE = "{msg_no}. You're a poop head. ({msg_no}/{msg_count})"

def send_text_poop(phone_number, message_count):

    sns = boto3.client('sns')

    for i in range(message_count):
        msg = MSG_TEMPLATE.format(msg_no=i+1, msg_count=message_count)
        print("Sending:", msg)
        sns.publish(PhoneNumber=phone_number, Message=msg)
