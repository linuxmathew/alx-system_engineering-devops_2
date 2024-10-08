#!/usr/bin/python3
"""
Function to query subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API nd returns the number of subscribers
    for a given subreddit.
    It handles invalid subreddits and redirects.
    Args:
    subreddit: the name of the subreddit to query
    Return:
    The number of subcribers (integer) or 0 if the subreddit is invalid
    """

    # Base URl for subreddint information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Set custom user-agent to avoid "Too many Requests" errors
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    # Send a GET request without following redirects
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error requesting subreddit info: {e}")
        return 0

    results = response.json().get("data")
    subscribers = results.get("subscribers", 0)
    return subscribers
