#!/usr/bin/python3
import requests
"""quirie reddit"""

def top_ten(subreddit):
    """ queries Reddit API and prints the titles of"""
    url_base = 'http://www.reddit.com/r/'
    url_query = '{:s}/hot.json?limit={:d}'.format(subreddit, 10)
    headers = {'user-agent': 'egsyquest'}
    r = requests.get(url_base + url_query, headers=headers)

    if (r.status_code == 302):
        print("None")
        return
    if (r.status_code == 404):
        print("None")
        return
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
