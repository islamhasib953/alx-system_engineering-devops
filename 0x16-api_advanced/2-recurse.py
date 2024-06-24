
#!/usr/bin/python3
"""
Write a function that queries the Reddit API
and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""


def recurse(subreddit, hot_list=[], after=None):
    '''Returns the number of subscribers for a given subreddit'''

    import requests

    if subreddit and type(subreddit) is str:
        urls = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        header = {
            'User-Agent': 'Mozilla/5.0'
        }
        parms = {
            'after': after,
            'limit': 100
        }

        result_req = requests.get(
            urls,
            headers=header,
            allow_redirects=False,
            params=parms)

        if result_req.status_code == 200:
            data = result_req.json().get('data')
            after = data.get('after')
            posts = data.get('children')

            for post in posts:
                hot_list.append(print(post.get('data').get('title')))

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
