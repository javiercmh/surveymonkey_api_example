import requests
import json

keyfile = open("token.key", 'r')
TOKEN = keyfile.readline().strip()

client = requests.session()

headers = {
"Authorization": "bearer %s" % TOKEN,
"Content-Type": "application/json"
}

data = {}

HOST = "https://api.surveymonkey.net"
SURVEY_LIST_ENDPOINT = "/v3/surveys"
SURVEY_LIST_ENDPOINT = "/v3/surveys/181462468/responses/bulk"   # movil_test survey

uri = "%s%s" % (HOST, SURVEY_LIST_ENDPOINT)

response = client.get(uri, headers=headers)

response_json = response.json()
#survey_list = response_json[data][surveys]

print(response_json)
