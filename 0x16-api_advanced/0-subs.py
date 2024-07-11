#!/usr/bin/python3
"""Module to query Reddit API and print top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                if posts:
                    for post in posts:
                        print(post['data']['title'])
                else:
                    print("None")
            except ValueError:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
