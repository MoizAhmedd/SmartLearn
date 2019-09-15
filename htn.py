import facebook
from security import token, stream_key
import requests
graph = facebook.GraphAPI(access_token=token)
# places = graph.search(type='place',
#                       center='37.4845306,-122.1498183',
#                       fields='name,location')
# #Each given id maps to an object the contains the requested fields.
# for place in places['data']:
#     print('%s %s' % (place['name'].encode(),place['location'].get('zip')))
#me/live_videos?status=LIVE_NOW
video = "https://graph.facebook.com/v4.0/me/live_videos?status=LIVE_NOW&access_token=" + token
#post_poll = video + "/" + stream_key + "/polls?question=Hello&options=Go"
print(video)
#print(post_poll)
r = requests.post(video)
output = r.json()
print(output)
live_id = output['id']
print(live_id)
data = {
       'correct_option': 1,
       'options': ['a','b','c','d'],
       'question': 'Choose letter?',
       'show_results': True,
   }
#post_poll = "https://graph.facebook.com/v4.0/" + str(live_id) + some_url + "&access_token=" + token
s = requests.post("https://graph.facebook.com/v4.0/1125823887602515/polls/", data={'my_data':data})
print(s.json())
# poll_id = s.json()['id']
# get_poll = "https://graph.facebook.com/v4.0/" + str(poll_id) + "?action=SHOW_RESULTS&access_token=" + token
# get_poll_request = requests.get(get_poll)
# returned_poll = get_poll_request.json()
# print(returned_poll)