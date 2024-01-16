#!/usr/bin/python3
"""module defining a function number_of_subscribers

the function queries the Reddit API and returns number of subscribers."""
import requests



def number_of_subscribers(subreddit):
    """function quering reddit api and return number of subscribers."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent':'Subs/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        subreddit_info = response.json()
        print("passed here")
        return subreddit_info['data']['subscribers']
    print(response.status_code)
    return (0)
