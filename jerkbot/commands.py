import random

from config import reddit_user_agent

from praw import Reddit

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
