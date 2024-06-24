#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns
the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the
function should return 0.
"""


def number_of_subscribers(subreddit):
    '''Returns the number of subscribers for a given subreddit'''

    import requests

    urls = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        'User-Agent': 'Mozilla/5.0'
    }

    result_req = requests.get(urls, headers=header, allow_redirects=False)

    if result_req.status_code >= 300:
        return 0

    return result_req.json().get("data").get("subscribers")
