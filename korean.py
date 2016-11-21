#!/usr/bin/python
import praw
import os
from slackclient import SlackClient

token = ""
sc = SlackClient(token)

user_agent = ("CuteKorean Bot")

r = praw.Reddit(user_agent=user_agent)

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

subreddit = r.get_subreddit("cutekorean")

for submission in subreddit.get_new(limit=5):
    if submission.id not in posts_replied_to:
        sc.api_call("chat.postMessage", username="new post bot", channel="cute-korean", text=submission.url, unfurl_links="true")
        posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
