# src/scrapers/arxiv_scraper.py

import arxiv
import os
import json
from datetime import datetime
from typing import List

def fetch_arxiv_papers(query: str = "(LLM OR transformers OR RAG) AND cat:cs.CL", 
                       max_results: int = 20,
                       save_path: str = "data/arxiv/") -> List[dict]:
    """
    Fetch recent NLP papers from arXiv matching the query.
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )

    results = []
    for result in search.results():
        paper = {
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "summary": result.summary,
            "url": result.entry_id,
            "published": result.published.isoformat()
        }
        results.append(paper)

    # Save to file
    os.makedirs(save_path, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(save_path, f"{today}.jsonl")

    with open(filepath, "w", encoding="utf-8") as f:
        for paper in results:
            f.write(json.dumps(paper) + "\n")

    print(f"✅ Saved {len(results)} papers to {filepath}")
    return results
