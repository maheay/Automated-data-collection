#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import requests

def lambda_handler(event, context):
    message = {'text': 'server down'}
    url = 'https://hooks.slack.com/services/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'
    try:
        requests.post(url, json=message)
        print("Alert Sent To Slack Successfully..")
    except:
        print("No Alert Sent To Slack..")
    
    return{
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

