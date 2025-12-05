#!/usr/bin/env python3
"""
Initialize SQLite database for research system
"""
import sqlite3
import os
from pathlib import Path

def init_database():
    """Initialize the research system database"""
    
    # Ensure domains directory exists
    domains_path = Path("/home/carsten/research/domains")
    domains_path.mkdir(exist_ok=True, parents=True)
    
    # Create initial trading_strategies domain
    trading_path = domains_path / "trading_strategies"
    trading_path.mkdir(exist_ok=True)
    (trading_path / "pdfs").mkdir(exist_ok=True)
    (trading_path / "vector_db").mkdir(exist_ok=True)
    
    # Connect to database
    db_path = trading_path / "metadata.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create domains table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            description TEXT,
            keywords TEXT,
            created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_used TIMESTAMP,
            doc_count INTEGER DEFAULT 0
        )
    """)
    
    # Create documents table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_id INTEGER,
            title TEXT NOT NULL,
            pdf_path TEXT,
            source_url TEXT,
            download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            tags TEXT,
            summary TEXT,
            file_hash TEXT,
            FOREIGN KEY (domain_id) REFERENCES domains(id)
        )
    """)
    
    # Create research_sessions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS research_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_id INTEGER,
            query TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            sources_found INTEGER,
            report_path TEXT,
            FOREIGN KEY (domain_id) REFERENCES domains(id)
        )
    """)
    
    # Insert initial domain
    cursor.execute("""
        INSERT OR IGNORE INTO domains (name, description, keywords)
        VALUES (?, ?, ?)
    """, (
        "trading_strategies",
        "Research on trading strategies, backtesting, and market analysis",
        "trading, momentum, mean reversion, pairs trading, rsi, backtest"
    ))
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database initialized: {db_path}")
    print(f"✅ Domain created: {trading_path}")

if __name__ == "__main__":
    init_database()
