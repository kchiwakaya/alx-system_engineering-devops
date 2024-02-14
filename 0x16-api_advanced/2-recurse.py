#!/usr/bin/python3
""" hello world"""
import requests
"""Hello"""

def recurse(subreddit, hot_list=[], after=""):
    """queries Reddit API and returns list.
    """
    url_base = 'http://www.reddit.com/r/'
    url_query = '{:s}/hot.json'.format(subreddit)
    headers = {'user-agent': 'starcraft'}
    r = requests.get(url_base + url_query, headers=headers)

    if (r.status_code == 302):
        print("None")
        return
    if (r.status_code == 404):
        return None
    else:
        r = r.json()
        for post in r['data']['children']:
            hot_list.append(post['data']['title'])

    return recurse(subreddit, hot_list, after)
