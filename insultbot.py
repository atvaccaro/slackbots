import time
import random
import requests
import json
from slackclient import SlackClient
import sys

token = ""
botName = "f-off-bot"
botChance = 5  #5 = 0.5% chance of text triggering an insult 10 = 1%, etc
botChannel = "#foo"

maxNoResponses = 1000
nonResponseCount = 0


def botSpeak(botText):
    sc.api_call("chat.postMessage", channel=botChannel, text=botText, as_user="true", username=botName, link_names=1)

sc = SlackClient(token)
if sc.rtm_connect():
    while True:
        new_evts = sc.rtm_read()
        for evt in new_evts:
            print(evt)
            foaasChance = random.randint(1, 1000)
            if "type" in evt:
                if evt["type"] == "message" and "text" and "user" in evt and "bot_id" not in evt and evt["channel"] == "C0HRK1LJC":
                    message = evt["text"]
                    user = "<@" + evt["user"] + ">"
                    if (foaasChance <= botChance) or nonResponseCount > maxNoResponses or "@U1GFSFT5K" in evt["text"]:
                        url = 'http://www.foaas.com/operations'
                        headers = {'Accept': 'application/json'}
                        r = requests.get(url, headers=headers)
                        foaas = json.loads(r.text)
                        badurl = 1
                        while (badurl == 1):
                            action = random.choice(foaas)
                            url = action['url']
                            url = url.replace(':from', botName)
                            url = url.replace(':name', user)
                            url = 'http://www.foaas.com' + url
                            if '/:' not in url:
                                badurl = 0
                        r = requests.get(url, headers=headers)
                        foaasMessage = json.loads(r.text)
                        botSpeak(botText=foaasMessage['message'])
                        nonResponseCount = 0
                    else:
                        nonResponseCount += 1
        time.sleep(1)
else:
    sys.exit(1)
