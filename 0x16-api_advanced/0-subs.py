#!/usr/bin/python3
"""
Number of subscribers for a given subreddit
"""

import requests

def number_of_subscribers(subreddit):
    """ Reddit API endpoint for subreddit information"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
  
    headers = {'User-Agent': 'CustomUserAgent'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print(f"Error: {response.status_code}")
            return 0
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
