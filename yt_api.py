import requests
# from pyyoutube import Api
import os
from pprint import pp

key = os.environ.get('YT_API_ID')
base_url = "https://www.googleapis.com/youtube/v3"
search_url = base_url + "/search"
headers = {"part": "snippet",
           "key": key,
           "type": "video",
           "q": "software",
           "maxResults": "5"
           }
# api = Api(api_key=key)
response = requests.get(search_url, headers)
pp(response.json()["items"])
