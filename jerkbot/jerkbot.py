import time, json
from slackclient import SlackClient
from praw import Reddit

# Info to make our bot work
token = 'xoxb-19648973122-MAAx5HcxxdxLSyGPq8qUp1yr'
my_user_agent = 'osx:com.atvaccaro.jerkbot:v0.1 (by /u/theplague42)'
my_usercode = 'idk yet'
my_username = 'jerkbot'

sc = SlackClient(token)
r = Reddit(user_agent=my_user_agent)
if sc.rtm_connect():
    # Get our list of users
    users = sc.api_call('users.list')
    time_since_last_circlejerk = 30
    while True:
        if time_since_last_circlejerk == 30:
            # Get top /r/circlejerk submission and post to #random
            submission = r.get_subreddit('circlejerk').get_hot().next()
            sc.api_call('chat.postMessage', channel='random', text=submission.title, token=token, username=my_username, as_user='true')
            time_since_last_circlejerk = 0

        time_since_last_circlejerk += 1
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
