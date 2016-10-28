from praw import Reddit

from config import reddit_user_agent

r = Reddit(user_agent=reddit_user_agent)


def circlejerk():
    pass


def get_top_post(subreddit=None):
    subreddit = r.get_subreddit('askreddit')
    submission = subreddit.get_hot().next()
    print(submission.title)
    print(submission.stickied)
    return submission


def get_subreddit_hot(subreddit):
    submissions = r.get_subreddit(subreddit).get_hot(limit=5)
    for submission in submissions:
        if not submission.stickied:
            return submission