from src.scrapers.arxiv_scraper import fetch_arxiv_papers
from src.scrapers.reddit_scraper import fetch_reddit_posts

def main():
    # Fetch latest papers
    papers = fetch_arxiv_papers()
    print(f"Fetched {len(papers)} arXiv papers")

    # Fetch popular Reddit posts
    reddit_posts = fetch_reddit_posts()
    print(f"Fetched {len(reddit_posts)} Reddit posts")

    # Combine or rank them further here if needed
    # For now, just print summaries
    print("\nArxiv Papers:")
    for p in papers[:5]:
        print(p['title'])

    print("\nReddit Posts:")
    for r in reddit_posts:
        print(f"{r['title']} ({r['score']} upvotes)")

if __name__ == "__main__":
    main()
