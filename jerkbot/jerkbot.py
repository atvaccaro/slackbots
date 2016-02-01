import time, json
from slackclient import SlackClient
from praw import Reddit
from config import

sc = SlackClient(token)
if sc.rtm_connect():
    # Get our list of users
    users = sc.api_call('users.list')
    time_since_last_circlejerk = 30
    while True:
        if time_since_last_circlejerk == 30:
            # Get top /r/circlejerk submission and post to #random
            submission = r.get_subreddit('circlejerk').get_hot().next()
            sc.api_call('chat.postMessage', channel='random', text=submission.title, token=token, username=slack_username, as_user='true')
            time_since_last_circlejerk = 0

        time_since_last_circlejerk += 1
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
