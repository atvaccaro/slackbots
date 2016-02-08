import db
from permissions import *
import commands
import time, json
from slackclient import SlackClient
from praw import Reddit
from config import slack_token, slack_usercode, slack_username, reddit_user_agent
import signal, sys
from users import UserManager

def signal_handler(signal, frame):
        print 'Saving to db...'
        permissions.save_to_db()
        print 'Shutting down. Bye!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

sc = SlackClient(slack_token)
r = Reddit(user_agent=reddit_user_agent)
um = UserManager()

# monitor Slack RTM
if sc.rtm_connect():
    while True:
        for message in sc.rtm_read():
            if message['type'] == 'message':
                text = message['text'].split()
                if text[0] == '!markov':
                    userlist = um.get_all_users()
                    print userlist
                    usercodes = [key for key, value in userlist.items() if value==text[1]]
                    print usercodes
                    usercode = usercodes[0]
                    text = commands.imitate(usercode)
                    sc.api_call('chat.postMessage', channel=message['channel'], text=text, token=slack_token, username=slack_username, as_user='true')
else:
    print "Connection Failed, invalid token?"
