import random

from praw import Reddit

from config import reddit_user_agent


def roll_dice(max_roll=6, num=1):
    return [random.randint(1, max_roll) for _ in range(num)]


def flip_coins(num=1):
    return [random.choice(('Heads', 'Tails')) for _ in range(num)]
