#!/usr/bin/env python3
"""
Simple helper to search via SearXNG and return results
"""
import requests
import json
import sys
from typing import List, Dict

SEARXNG_URL = "http://localhost:8889/search"

def search(query: str, num_results: int = 10) -> List[Dict]:
    """Search using SearXNG and return results"""
    try:
        response = requests.get(
            SEARXNG_URL,
            params={
                'q': query,
                'format': 'json',
                'engines': 'google,duckduckgo,brave',
                'categories': 'general',
                'language': 'en'
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        results = data.get('results', [])[:num_results]
        
        # Format for easy reading
        formatted = []
        for i, result in enumerate(results, 1):
            formatted.append({
                'index': i,
                'title': result.get('title', ''),
                'url': result.get('url', ''),
                'content': result.get('content', ''),
                'engine': result.get('engine', '')
            })
        return formatted
        
    except Exception as e:
        return [{'error': str(e)}]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 search_helper.py 'your query'")
        sys.exit(1)
    
    query = ' '.join(sys.argv[1:])
    results = search(query)
    print(json.dumps(results, indent=2, ensure_ascii=False))
