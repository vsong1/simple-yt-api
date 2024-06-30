### This simple script retrieves and prints a neat
#   table of search results based on the entered 
#   search query.

import requests
import os
import sqlalchemy as db
import pandas as pd

## provide YouTube Data API key
key = os.environ.get('YT_API_ID')

## send GET request for YouTube videos
base_url = "https://www.googleapis.com/youtube/v3"
search_url = base_url + "/search"
query = input("Input Search Query: ")

headers = {"part":"snippet",
  "key":key, 
  "type":"video", 
  "q":query,
  "maxResults":"5"
}

response = requests.get(search_url, headers)
query_dict = pd.DataFrame(pd.json_normalize(response.json()["items"]))

## create SQL database, print as Pandas DataFrame
engine = db.create_engine('sqlite:///query_result.db')
query_dict.to_sql('results', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_out = connection.execute(db.text('SELECT \
            "snippet.title" AS title, \
            "snippet.publishedAt" AS publishDate, \
            "snippet.channelTitle" AS channel, \
            "id.videoId" AS videoId \
            FROM results;')).fetchall()
   print(pd.DataFrame(query_out))