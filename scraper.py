import praw
import os

def scrape_user_activity(username):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="user_persona_scraper"
    )

    user = reddit.redditor(username)
    posts, comments = [], []

    for submission in user.submissions.new(limit=50):
        posts.append({
            "title": submission.title,
            "body": submission.selftext,
            "url": submission.url
        })

    for comment in user.comments.new(limit=50):
        comments.append({
            "body": comment.body,
            "link": f"https://reddit.com{comment.permalink}"
        })

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }
