import time, json
from slackclient import SlackClient

# Info to make our bot work
token = 'xoxb-19193098289-BqJYZV68gmpYqx0VAQrbPdiY'
my_usercode = 'U0K5P2W8H'
my_username = 'Daniel-san'
daniel_usercode = 'U0D1SEBV0'

sc = SlackClient(token)
if sc.rtm_connect():
    # Get our list of users
    users = sc.api_call('users.list')
    print users
    time_since_users_update = 0
    while True:
        messages = sc.rtm_read()
        for message in messages:
            # Reload if change in users
            print message
            if message['type'] == 'user_change':
                users = sc.api_call('user.list')

            elif message['type'] == 'message':
                if message['user'] == daniel_usercode or '@daniel.kim17' in message['text']:
                    channel = message['channel']
                    text = 'Go to class, Daniel!'
                    sc.api_call('chat.postMessage', channel=channel, text=text, token=token, username=my_username, as_user='true')

        time.sleep(1)
        time_since_users_update += 1

        # Update our local list of users every 120 seconds even if we don't detect a change
        if time_since_users_update == 120:
            users = sc.api_call('users.list')
            time_since_users_update = 0
else:
    print "Connection Failed, invalid token?"
'''
print sc.api_call('api.test')
print sc.api_call('channels.list')
channel_info = json.loads(sc.api_call('channels.info', channel='C0K5UALP8'))
print channel_info['channel']['topic']
'''
