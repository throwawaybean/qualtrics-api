import http.client
import zipfile
import os
import io
import base64
import json
import requests


clientID="f69817e6d0431d057bd66f857eaad0fa"
clientsecret="kKL9S7jLULUh4mG1gPSvEwzCBzpYXrc3aHScdRbSAeLCVD4pEhtstvoZEvmdeZve"
auth = "{0}:{1}".format(clientID, clientsecret)
encodedBytes=base64.b64encode(auth.encode("utf-8"))
authStr = str(encodedBytes, "utf-8")

#create the connection
conn = http.client.HTTPSConnection("fra1.qualtrics.com")
body = "grant_type=client_credentials"
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
headers['Authorization'] = 'Basic {0}'.format(authStr)

#make the request
conn.request("POST", "/oauth2/token", body, headers)
res = conn.getresponse()
data = res.read()
token = json.loads(data.decode("utf-8"))
print(token)
token = token["access_token"]
os.environ["token"] = token


# create the request
conn = http.client.HTTPSConnection("fra1.qualtrics.com")
body = ''
headers = {
  'Authorization': f'Bearer {token}'
}

# make the request
conn.request("GET", "/API/v3/whoami", body, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# Setting user Parameters
dataCenter = "fra1"

bearerToken = token # call the bearer token function
baseUrl = "https://{0}.qualtrics.com/API/v3/surveys".format(dataCenter)
headers = {
    "authorization": "bearer " + bearerToken,
    }

response = requests.request("GET", baseUrl, headers=headers)
print(response.text)

#api test call ends here



apiToken = "GJykpEExRL0v5zHgGsugf5LSD3eubyfbaTQlxrbq"  # 1
dataCenter = "fra1" # 2
surveyId = "SV_aW8vfOfS37AiEAd"    # 3

'''
baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}".format(dataCenter, surveyId)
headers = {
    "x-api-token": apiToken,
    }

response = requests.get(baseUrl, headers=headers)
print(response.text)
'''

conn = http.client.HTTPSConnection("fra1.qualtrics.com")

headers = { 'x-api-token': apiToken }

conn.request("GET", "/API/v3/survey-definitions/SV_aW8vfOfS37AiEAd/blocks/BL_bqKTQU7hRUvPGhn", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
