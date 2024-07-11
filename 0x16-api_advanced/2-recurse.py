#!/usr/bin/python3
"""
This module contains a recursive function to fetch hot posts from a subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively fetch all hot post titles from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store hot post titles (default is None).
        after (str): Token for pagination (default is None).

    Returns:
        list: A list of hot post titles, or None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot/0.0.1'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
