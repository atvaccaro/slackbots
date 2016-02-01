from permissions import PermissionManager
from db import cursor
import config, random, requests

pm = PermissionManager(config.permissions_filename)

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

def get_beer():
    
