import requests

def xkcd(number=None,text=None):
    if number:
        r = requests.get('http://xkcd.com/'+str(number)+'/info.0.json')
        return r.json()
    elif text:
        return None
    else:
        r = requests.get('http://xkcd.com/info.0.json')
        return r.json()