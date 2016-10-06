import hashlib
from flask import Flask, jsonify, request

import commands
from slackclient import SlackClient
from praw import Reddit
from config import slack_token, slack_username, reddit_user_agent

import chungisms

sc = SlackClient(slack_token)
r = Reddit(user_agent=reddit_user_agent)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/markov', methods=['POST'])
def markov():
    username = request.form.get('text')
    if username:
        text = commands.imitate(username)
        sc.api_call('chat.postMessage', channel='#slackbots', text=text, token=slack_token, username=slack_username, as_user='true')
    else:
        return 'Need a username'

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
