from nose.tools import *
from slackclient import SlackClient
from praw import Reddit

from db import cursor, conn
from config import slack_token, reddit_user_agent
from commands import imitate, circlejerk, get_subreddit_hot, xkcd, roll_dice, flip_coins

def test_slack_connect():
    sc = SlackClient(slack_token)

def test_praw():
    pass

def test_imitate():
    pass

def test_circlejerk():
    pass

def test_get_subreddit_hot():
    pass

def test_xkcd():
    pass

def test_roll_dice():
    rolls = roll_dice(10, 1)
    assert(all([1<=x and x<=10 for x in rolls]))

def test_flip_coins():
    pass
