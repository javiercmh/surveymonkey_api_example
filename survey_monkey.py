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
SURVEY_LIST = "/v3/surveys"
# SURVEY_RESPONSES = "/v3/surveys/181462468/responses/bulk"   # that number is a survey id

# create uris
survey_list_uri = "%s%s" % (HOST, SURVEY_LIST)
# survey_responses_uri = "%s%s" % (HOST, SURVEY_RESPONSES)

# make the requests
survey_list = client.get(survey_list_uri, headers=headers)
# survey_responses = client.get(survey_responses_uri, headers=headers)

# get jsons (python dict() format)
response_json = survey_list.json()
# response_json = survey_responses.json()

#survey_list = response_json[data][surveys]

print(response_json)
