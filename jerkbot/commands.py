import requests, random

import permissions
from db import cursor
from markov import Markov
from config import reddit_user_agent

from praw import Reddit

r = Reddit(user_agent=reddit_user_agent)

def imitate(usercode=None, username=None):
    if usercode:
        markov = Markov(usercode=usercode)
        return markov.generate_markov_text()
    elif username:
        return
    else:
        return

def circlejerk():
    submission = get_subreddit_hot('circlejerk')
    sc.api_call('chat.postMessage', channel='#slackbots', text=submission.short_link, token=slack_token, username=slack_username, as_user='true')

def get_subreddit_hot(subreddit):
    submissions = r.get_subreddit(subreddit).get_hot(limit=5)
    for submission in submissions:
        if not submission.stickied:
            return submission
            break

def xkcd(number=None,text=None):
    if number:
        r = requests.get('http://xkcd.com/'+str(number)+'/info.0.json')
        return r.json()
    elif text:
        return None
    else:
        r = requests.get('http://xkcd.com/info.0.json')
        return r.json()

def roll_dice(max_roll=None, num=1):
    max_roll = 6 if not max_roll else max_roll
    rolls = []
    for i in range(num):
        rolls.append(random.randint(1, max_roll))
    return rolls

def flip_coins(num=1):
    flips = []
    for i in range(num):
        flips.append(('Heads', 'Tails')[random.randint(0, 1)])
    return flips
