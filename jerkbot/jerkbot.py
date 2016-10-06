import hashlib
from slackclient import SlackClient

from chungisms import get_wisdom
from config import slack_token, slack_username
from markov import imitate
from urban import urban_define

sc = SlackClient(slack_token)

commands = [
    '!markov',
    '!urban',
    '!md5',
    '!chungism'
]
if sc.rtm_connect():
    while True:
        for message in sc.rtm_read():
            print message
            if message.get('type') == 'message' and message.get('text') and message.get('user'):
                text = message['text'].split()
                if any([command in text for command in commands]):
                    command = text[0]
                    if command == '!markov':
                        response = imitate(text[1])
                    elif command == '!urban':
                        response = urban_define(' '.join(text[1:]))
                    elif command == '!md5':
                        response = hashlib.md5(' '.join(text[1:])).hexdigest()
                    elif command == '!chungism':
                        response = get_wisdom()
                    else:
                        response = 'Command not recognized'

                    sc.api_call('chat.postMessage', channel=message['channel'], text=response, token=slack_token, username=slack_username, as_user='true')
else:
    print "Connection Failed, invalid token?"
