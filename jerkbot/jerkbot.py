import db
from permissions import *
import commands, define
import time, json
from slackclient import SlackClient
from praw import Reddit
from config import slack_token, slack_usercode, slack_username, reddit_user_agent
import signal, sys
from users import UserManager

def signal_handler(signal, frame):
        print 'Saving to db...'
        save_to_db()
        print 'Shutting down. Bye!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

sc = SlackClient(slack_token)
r = Reddit(user_agent=reddit_user_agent)
um = UserManager()

bot_commands = {
    '!markov': commands.imitate,
    '!urban': define.urban_define,
}

def not_found():
    return 'Command not found.'

if sc.rtm_connect():
    while True:
        for message in sc.rtm_read():
            print message
            if message.get('type') == 'message' and message.get('text'):
                text = message['text'].split()
                if text[0] in bot_commands.keys():
                    text = bot_commands.get(text[0])(message['text'].split())
                    sc.api_call('chat.postMessage', channel=message['channel'], text=text, token=slack_token, username=slack_username, as_user='true')
else:
    print "Connection Failed, invalid token?"
