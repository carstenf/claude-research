#!/usr/bin/env python3
"""
Trading Strategy Research Agent - Starter Version
"""
import sys
import requests
from pathlib import Path
from datetime import datetime

class ResearchAgent:
    def __init__(self):
        self.searxng_url = "http://localhost:8888"
        self.chromadb_url = "http://localhost:8000"
        
    def search_web(self, query: str, num_results: int = 10):
        """Search using SearXNG"""
        print(f"🔍 Searching for: {query}")
        
        try:
            response = requests.get(
                f"{self.searxng_url}/search",
                params={
                    'q': query,
                    'format': 'json',
                    'engines': 'google,duckduckgo,brave',
                    'categories': 'general'
                },
                timeout=30
            )
            
            if response.status_code == 200:
                results = response.json().get('results', [])[:num_results]
                print(f"✅ Found {len(results)} results")
                return results
            else:
                print(f"❌ Search failed: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Search error: {e}")
            return []
    
    def test_services(self):
        """Test if services are reachable"""
        print("🧪 Testing services...")
        
        # Test SearXNG
        try:
            response = requests.get(f"{self.searxng_url}/", timeout=5)
            if response.status_code == 200:
                print("✅ SearXNG: Running")
            else:
                print(f"⚠️ SearXNG: Unexpected status {response.status_code}")
        except Exception as e:
            print(f"❌ SearXNG: Not reachable - {e}")
        
        # Test ChromaDB
        try:
            response = requests.get(f"{self.chromadb_url}/api/v1/heartbeat", timeout=5)
            if response.status_code == 200:
                print("✅ ChromaDB: Running")
            else:
                print(f"⚠️ ChromaDB: Unexpected status {response.status_code}")
        except Exception as e:
            print(f"❌ ChromaDB: Not reachable - {e}")
    
    def generate_report(self, query: str, results: list) -> str:
        """Generate simple markdown report"""
        report = f"""# Research Report

**Query:** {query}  
**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Sources Found:** {len(results)}

## Results

"""
        for i, result in enumerate(results, 1):
            title = result.get('title', 'No title')
            url = result.get('url', '')
            content = result.get('content', 'No description')[:200]
            
            report += f"### {i}. {title}\n\n"
            report += f"**URL:** {url}\n\n"
            report += f"{content}...\n\n"
            report += "---\n\n"
        
        return report
    
    def save_report(self, report: str, query: str):
        """Save report to file"""
        reports_dir = Path("/home/carsten/research/reports")
        reports_dir.mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"research_{timestamp}.md"
        filepath = reports_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"💾 Report saved: {filepath}")
        return filepath
    
    def research(self, query: str):
        """Main research workflow"""
        print("\n" + "="*60)
        print("🚀 Starting Research")
        print("="*60 + "\n")
        
        # Test services
        self.test_services()
        print()
        
        # Search
        results = self.search_web(query)
        
        if not results:
            print("❌ No results found")
            return
        
        # Generate report
        print("\n📝 Generating report...")
        report = self.generate_report(query, results)
        
        # Save report
        filepath = self.save_report(report, query)
        
        # Display summary
        print("\n" + "="*60)
        print("✅ Research Complete")
        print("="*60)
        print(f"\nReport: {filepath}")
        print(f"Sources: {len(results)}")
        print("\nNext steps:")
        print("- Review report in reports/ directory")
        print("- Implement LangGraph for advanced workflow")
        print("- Add ChromaDB integration for RAG")
        print("- Enhance with Claude API for synthesis")

def main():
    if len(sys.argv) < 2:
        print("Usage: python researcher.py \"your research query\"")
        print("\nExample:")
        print("  python researcher.py \"RSI momentum trading strategies\"")
        print("\nTest services:")
        print("  python researcher.py --test")
        sys.exit(1)
    
    agent = ResearchAgent()
    
    if sys.argv[1] == "--test":
        agent.test_services()
    else:
        query = " ".join(sys.argv[1:])
        agent.research(query)

if __name__ == "__main__":
    main()
