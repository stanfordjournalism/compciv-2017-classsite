# http://boto3.readthedocs.io/en/latest/reference/services/polly.html

import boto3
session = boto3.Session(profile_name='dun')



resp = polly.synthesize_speech(OutputFormat='mp3',
        Text='Who let the dogs out? Who? Who? Who?',
        VoiceId='Joanna')
