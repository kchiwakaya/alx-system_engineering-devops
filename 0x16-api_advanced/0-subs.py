#!/usr/bin/python3
"""
queries the Reddit API
returns the number of total subscribers for a given
subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API
    given subreddit.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Python/1.0(Holberton School 0x16 task 0)'}
    response = requests.get(url, headers=header)
    if (not response.ok):
        return 0
    count = response.json().get('data').get('subscribers')
    return count
