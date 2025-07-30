import praw

# Replace with your Reddit app credentials here or load from env variables/config
CLIENT_ID = "mZwUdUSpVyFOJ4K_pLD06A"
CLIENT_SECRET = "L2WL1OHuxgOpD7mFAG3e7TDbyUy5aQ"
USER_AGENT = "trendformer by /u/Icy-Fox-160"

# Keywords to search for
SEARCH_QUERY = '(LLM OR transformers OR RAG) AND (NLP OR "natural language processing" OR "machine learning")'

def fetch_reddit_posts(limit=50, min_upvotes=10, flair_filter = "News"):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    subreddit = reddit.subreddit('MachineLearning+LanguageTechnology+NLP')


    # Search posts matching the query, sort by relevance/new/hot/top as you prefer
    posts = subreddit.search(SEARCH_QUERY, sort="top", limit=limit)

    results = []
    for post in posts:
        if post.score >= min_upvotes:
            if flair_filter is None or (post.link_flair_text and post.link_flair_text.lower() == flair_filter.lower()):
                results.append({
                    "title": post.title,
                    "score": post.score,
                    "url": post.url,
                    "created_utc": post.created_utc,
                    "subreddit": post.subreddit.display_name,
                    "id": post.id,
                    "num_comments": post.num_comments,
                    "selftext": post.selftext,
                    "flair": post.link_flair_text
                })

    return results

if __name__ == "__main__":
    reddit_posts = fetch_reddit_posts()
    for post in reddit_posts:
        print(f"{post['title']} ({post['score']} upvotes) - {post['url']}")
