#!/usr/bin/env python3
"""
Claude-as-a-Service Research System
No API keys needed - Claude does the research via MCP
"""
import sqlite3
from pathlib import Path
from datetime import datetime
import hashlib

class ClaudeResearchSystem:
    def __init__(self):
        self.base_path = Path("/home/carsten/research")
        self.domains_path = self.base_path / "domains"
        self.reports_path = self.base_path / "reports"
        
    def create_domain(self, domain_name: str, description: str = "", keywords: str = ""):
        """Create a new research domain"""
        domain_path = self.domains_path / domain_name
        domain_path.mkdir(exist_ok=True, parents=True)
        (domain_path / "pdfs").mkdir(exist_ok=True)
        (domain_path / "notes").mkdir(exist_ok=True)
        
        # Create database
        db_path = domain_path / "metadata.db"
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                source_url TEXT,
                local_path TEXT,
                summary TEXT,
                tags TEXT,
                added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                file_hash TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS research_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                sources_count INTEGER,
                report_path TEXT,
                notes TEXT
            )
        """)
        
        conn.commit()
        conn.close()
        
        print(f"✅ Domain created: {domain_path}")
        return domain_path
    
    def add_document(self, domain_name: str, title: str, source_url: str, 
                     summary: str = "", tags: str = "", local_path: str = ""):
        """Add document to domain database"""
        db_path = self.domains_path / domain_name / "metadata.db"
        
        # Generate file hash
        file_hash = hashlib.md5(f"{title}{source_url}".encode()).hexdigest()[:8]
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO documents (title, source_url, local_path, summary, tags, file_hash)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, source_url, local_path, summary, tags, file_hash))
        
        conn.commit()
        doc_id = cursor.lastrowid
        conn.close()
        
        return doc_id
    
    def add_research_session(self, domain_name: str, query: str, 
                            sources_count: int, report_path: str, notes: str = ""):
        """Log research session"""
        db_path = self.domains_path / domain_name / "metadata.db"
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO research_sessions (query, sources_count, report_path, notes)
            VALUES (?, ?, ?, ?)
        """, (query, sources_count, report_path, notes))
        
        conn.commit()
        conn.close()
    
    def get_domain_stats(self, domain_name: str):
        """Get statistics for a domain"""
        db_path = self.domains_path / domain_name / "metadata.db"
        
        if not db_path.exists():
            return None
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Document count
        cursor.execute("SELECT COUNT(*) FROM documents")
        doc_count = cursor.fetchone()[0]
        
        # Research session count
        cursor.execute("SELECT COUNT(*) FROM research_sessions")
        session_count = cursor.fetchone()[0]
        
        # Last session
        cursor.execute("SELECT timestamp FROM research_sessions ORDER BY timestamp DESC LIMIT 1")
        result = cursor.fetchone()
        last_session = result[0] if result else "Never"
        
        conn.close()
        
        return {
            'documents': doc_count,
            'sessions': session_count,
            'last_session': last_session
        }
    
    def list_domains(self):
        """List all research domains"""
        domains = []
        for domain_path in self.domains_path.iterdir():
            if domain_path.is_dir():
                stats = self.get_domain_stats(domain_path.name)
                domains.append({
                    'name': domain_path.name,
                    'path': domain_path,
                    'stats': stats
                })
        return domains

if __name__ == "__main__":
    system = ClaudeResearchSystem()
    
    print("📊 Research System Status\n")
    
    domains = system.list_domains()
    if domains:
        for domain in domains:
            print(f"Domain: {domain['name']}")
            if domain['stats']:
                print(f"  Documents: {domain['stats']['documents']}")
                print(f"  Sessions: {domain['stats']['sessions']}")
                print(f"  Last: {domain['stats']['last_session']}")
            print()
    else:
        print("No domains yet. Create one with:")
        print("  system.create_domain('trading_strategies')")
