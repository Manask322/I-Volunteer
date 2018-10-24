import urllib.request
import urllib.response
import sys
import os, glob

import http.client, urllib
import json
import re

accessKey = key
url = 'westcentralus.api.cognitive.microsoft.com'
path = '/text/analytics/v2.0/keyPhrases'
 
def handler():
    # 1. 
    documents = extractText()
    # 2. Perform Text Analysis
    result = TextAnalytics(documents) 
    # 3. Print Results
    print (json.dumps(json.loads(result), indent=4))

def extractText():
    documents = { 'documents': []}
    count = 1
   
    text = "There is a flood near VLS International School"
    #text = text.strip('\n')
    text = text.encode('ascii','ignore').decode('ascii')
    documents.setdefault('documents').append({"language":"en","id":str(count),"text":text})
    #count+= 1
    return documents


def TextAnalytics(documents):
    headers = {'Ocp-Apim-Subscription-Key': accessKey}
    conn = http.client.HTTPSConnection(url)
    body = json.dumps (documents)
    conn.request ("POST", path, body, headers)
    response = conn.getresponse ()
    return response.read ()

if __name__ == '__main__':
    handler()
