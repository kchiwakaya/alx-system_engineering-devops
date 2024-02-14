#!/usr/bin/python3
"""Reddits readd API"""
import requests
"""Sub tr"""

def number_of_subscribers(subreddit):
    """ query Reddit API and return number of subscribers for given subreddit
   """
    url = "http://www.reddit.com/r/{:s}/about.json".format(subreddit)
    headers = {'user-agent': 'egsyquest'}
    r = requests.get(url, headers=headers)

    if (r.status_code == 302):
        return 0
    if (r.status_code == 404):
        return 0

    return r.json()['data'].get('subscribers', 0)
