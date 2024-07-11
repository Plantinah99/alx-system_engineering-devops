#!/usr/bin/python3
"""Module to query Reddit API and get number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers. Returns 0 if the subreddit is invalid.
    """
    # Reddit API URL for subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        # Make the API request
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the subreddit is valid
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # Invalid subreddit
            return 0

    except requests.RequestException:
        # Handle any request-related errors
        return 0


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
