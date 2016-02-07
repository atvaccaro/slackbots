import db
from permissions import *
import time, json
from slackclient import SlackClient
from praw import Reddit
from config import slack_token, slack_usercode, slack_username, reddit_user_agent
import signal, sys

def signal_handler(signal, frame):
        print 'Saving to db...'
        pm.save_to_db()
        print 'Shutting down. Bye!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

sc = SlackClient(slack_token)
r = Reddit(user_agent=reddit_user_agent)
if sc.rtm_connect():
    # Get our list of users
    userlist = sc.api_call('users.list')
    for user in userlist['members']:
        permissions.update_permission(user['id'], Permission.USER)

    time_since_last_circlejerk = 3600
    while True:
        if time_since_last_circlejerk == 60*60:
            submissions = r.get_subreddit('SubredditSimulator').get_hot(limit=5)
            for submission in submissions:
                if not submission.stickied:
                    sc.api_call('chat.postMessage', channel='#slackbots', text=submission.short_link, token=slack_token, username=slack_username, as_user='true')
                    break
            time_since_last_circlejerk = 0

        time_since_last_circlejerk += 1
        time.sleep(1)
else:
    print "Connection Failed, invalid token?"
