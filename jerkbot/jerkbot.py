import hashlib

import morse_script
import commands, urban
from slackclient import SlackClient
from praw import Reddit
from config import slack_token, slack_username, reddit_user_agent
from flask import Flask, jsonify, request

import chungisms

sc = SlackClient(slack_token)
r = Reddit(user_agent=reddit_user_agent)

bot_commands = {
    '!markov': commands.imitate,
    '!urban': urban.urban_define,
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


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/markov', methods=['POST'])
def markov():
    username = request.form.get('text')
    if username:
        text = commands.imitate(username)
        sc.api_call('chat.postMessage', channel=message['channel'], text=text, token=slack_token, username=slack_username, as_user='true')
    else:
        return 'Need a username'

@app.route('/morse', methods=['GET', 'POST'])
def morse():
    if request.method == 'POST':
        if request.form['text']:
            chars = list(request.form['text'])
            if any([not c.isalnum() for c in chars]):
                return 'Unacceptable input, my dear friend.'
            return jsonify(response_type = 'in_channel', text = morse_script.encode_morse(request.form['text']))
        else:
            return 'You need to add text to convert'
    else:
        return 'You need to add text to convert'

@app.route('/demorse', methods=['GET', 'POST'])
def demorse():
    if request.method == 'POST':
        if request.form['text']:
            chars = list(request.form['text'])
            if any([c not in '-. ' for c in chars]):
                return 'Unacceptable input, my dear friend.'
            return jsonify(response_type = 'in_channel', text = morse_script.decode_morse(request.form['text']))
        else:
            return 'You need to add text to convert'
    else:
        return 'You need to add text to convert'


@app.route('/chungism', methods=['GET', 'POST'])
def chungism():
    if request.method == 'GET':
        return jsonify(response_type = 'in_channel', text = chungisms.get_wisdom())
    else:
        return 'You shall not POST'

@app.route('/md5', methods=['GET', 'POST'])
def md5():
    if request.method == 'POST':
        if request.form['text']:
            return jsonify(response_type='in_channel', text=hashlib.md5(request.form['text']).hexdigest())
        else:
            return 'You need to add text to hash'
    else:
        return 'You shall not GET!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
