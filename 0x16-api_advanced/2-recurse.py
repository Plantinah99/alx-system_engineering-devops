#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests
from time import sleep

def recurse(subreddit, hot_list=[], after=None, count=0, delay=2):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'user-agent': 'my-app/0.0.1'}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        if response.text:
            data = response.json()
            results = data.get("data")
            after = results.get("after")
            count += results.get("dist", 0)
            for child in results.get("children", []):
                hot_list.append(child.get("data", {}).get("title"))

            if after is not None:
                sleep(delay)  # Delay to respect rate-limiting
                return recurse(subreddit, hot_list, after, count, delay)
            else:
                return hot_list, count
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None
