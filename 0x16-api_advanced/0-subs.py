#!/usr/bin/python3
"""
Number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Check for HTTP errors

        data = response.json()
        return data['data']['subscribers']
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
