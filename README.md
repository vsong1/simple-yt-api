# YouTube Search Results Calculator
A Python application to calculate differences between a user's search results and base results.

## Setup
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages:
```bash
pip install requests
pip install sqlalchemy
pip install pandas
```
This application also requires a [YouTube API key](https://developers.google.com/youtube/v3/), stored as an environmental variable `YT_API_ID`.

## Usage
```python
import yt_sqltable as yt

# returns base search results for the query 'horses'
yt.blank_search("horses")
```