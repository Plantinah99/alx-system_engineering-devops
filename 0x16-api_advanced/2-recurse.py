import requests

def recurse(subreddit, hot_list=[], after=None):
    # Base URL for Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # Parameters for the API request
    params = {'limit': 100}  # Maximum number of items per request
    if after:
        params['after'] = after
    
    try:
        # Make the API request
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the subreddit is valid
        if response.status_code == 404:
            return None
        
        # Raise an exception for other HTTP errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract post titles and add them to the list
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        
        # Check if there are more pages
        if data['data']['after']:
            # Recursive call with the 'after' parameter
            return recurse(subreddit, hot_list, data['data']['after'])
        else:
            # Base case: no more pages, return the complete list
            return hot_list
    
    except requests.RequestException:
        # Handle any request-related errors
        return None

# Example usage
if __name__ == '__main__':
    subreddit = "python"
    result = recurse(subreddit)
    if result is not None:
        print(f"Number of hot posts in r/{subreddit}: {len(result)}")
    else:
        print(f"Failed to retrieve hot posts from r/{subreddit}")
