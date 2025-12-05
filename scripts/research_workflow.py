#!/usr/bin/env python3
"""
Claude-assisted research workflow
This script provides tools for Claude to conduct research
"""
import json
import sys
from search_helper import search
from datetime import datetime

def research_query(query: str, num_results: int = 10):
    """
    Execute a research query and return formatted results
    """
    print(f"\n🔍 Searching for: {query}")
    print("=" * 80)
    
    results = search(query, num_results)
    
    if results and 'error' in results[0]:
        print(f"❌ Error: {results[0]['error']}")
        return None
    
    print(f"\n✅ Found {len(results)} results\n")
    
    for result in results:
        print(f"[{result['index']}] {result['title']}")
        print(f"    URL: {result['url']}")
        print(f"    Engine: {result['engine']}")
        if result['content']:
            print(f"    Preview: {result['content'][:150]}...")
        print()
    
    return results

def save_research_report(query: str, findings: str, sources: list):
    """
    Save research report to file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/research_{timestamp}.md"
    
    report = f"""# Research Report
    
**Query:** {query}  
**Date:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Findings

{findings}

## Sources

"""
    
    for i, source in enumerate(sources, 1):
        report += f"{i}. [{source.get('title', 'Untitled')}]({source.get('url', '#')})\n"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ Report saved: {filename}")
    return filename

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("""
Research Workflow - Usage Examples:

# Basic search
python3 research_workflow.py search "RSI mean reversion strategies"

# Interactive mode
python3 research_workflow.py interactive
        """)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'search':
        query = ' '.join(sys.argv[2:])
        research_query(query)
    elif command == 'interactive':
        print("🤖 Claude-assisted research mode")
        print("Type 'exit' to quit\n")
        while True:
            query = input("Research query: ").strip()
            if query.lower() == 'exit':
                break
            if query:
                research_query(query)
