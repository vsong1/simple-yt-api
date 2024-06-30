import requests
#from pyyoutube import Api
import os

key = os.environ.get('YT_API_ID')
base_url = "https://www.googleapis.com/youtube/v3"
search_url = base_url + "/search"
headers = {"key":key, 
  "type":"video", 
  "q":"software"
}
#api = Api(api_key=key)
response = requests.get(search_url, headers)