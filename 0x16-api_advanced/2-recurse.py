#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function returns None.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    If not a valid subreddit, return None.
    """
    if hot_list is None:
        hot_list = []

    headers = {"User-Agent": "Custom"}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}

    req = requests.get(url, headers=headers, params=params)

    if req.status_code == 200:
        data = req.json().get("data")
        if data:
            children = data.get("children", [])
            for get_data in children:
                dat = get_data.get("data")
                title = dat.get("title")
                hot_list.append(title)
            after = data.get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    return None
