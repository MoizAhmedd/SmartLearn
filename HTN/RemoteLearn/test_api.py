import requests
import json
headers = {
    "Authorization": "bearer %s" % "nI-ogNyihhsexcS.VNIi2plq4qzLUUOYnit5bO96uEdNDEaQYQUEzjA3krQXZLXMTyCufQqb5BybO.1aZ48nt2KXcXa0SXf5Jwd47ieMvoDgA885fofnPnYhTQnnRPAx",
    "Content-Type": "application/json"
}
client = requests.session()
data = {
    "title": "ABC Survey",
    } 
HOST = "https://api.surveymonkey.net"   
CREATE_SURVEY_ENDPOINT = "/v3/surveys"
uri = "%s%s" % (HOST, CREATE_SURVEY_ENDPOINT)
request_survey = requests.post(uri,data=json.dumps(data),headers=headers)
to_json = request_survey.json()
survey_id = to_json['id']

page_data = {

}
CREATE_PAGE_ENDPOINT = "/v3/surveys/" + survey_id + "/pages"
page_uri = "%s%s" % (HOST, CREATE_PAGE_ENDPOINT)
page_request = requests.post(page_uri,data=json.dumps(page_data),headers=headers)
page_to_json = page_request.json()
page_id = page_to_json['id']

question_data = {
    "headings": [

    ],
    "family": '',
    "subtype": '',
    "answers":
}
CREATE_QUESTION_ENDPOINT = "/v3/surveys/<survey_id>/pages/" + page_id + "/questions"
question_uri = "%s%s" % (HOST, CREATE_QUESTION_ENDPOINT)
question_request = requests.post(page_uri,data=json.dumps(page_data),headers=headers)
