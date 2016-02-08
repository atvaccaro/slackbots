import db
from permissions import *
from commands import *
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

# Get our list of Slack
    userlist = sc.api_call('users.list')
    for user in userlist['members']:
        permissions.update_permission(user['id'], Permission.USER)

# monitor Slack RTM
if sc.rtm_connect():
    while True:
        for message in sc.rtm_read():
            continue
else:
    print "Connection Failed, invalid token?"
