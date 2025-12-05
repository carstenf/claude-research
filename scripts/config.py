"""
Central configuration for research system
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base paths
BASE_DIR = Path("/home/carsten/research")
DOMAINS_DIR = BASE_DIR / "domains"
REPORTS_DIR = BASE_DIR / "reports"
SCRIPTS_DIR = BASE_DIR / "scripts"

# API Keys
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Service URLs
SEARXNG_URL = os.getenv("SEARXNG_URL", "http://localhost:8888")
CHROMADB_URL = os.getenv("CHROMADB_URL", "http://localhost:8000")

# Model Configuration
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "claude-sonnet-4-20250514")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")

# Search Configuration
MAX_SEARCH_RESULTS = int(os.getenv("MAX_SEARCH_RESULTS", "20"))
SEARCH_ENGINES = ["google", "duckduckgo", "brave"]

# RAG Configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
SIMILARITY_THRESHOLD = 0.7

# LangSmith (Optional)
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "trading-research")

def validate_config():
    """Validate configuration"""
    errors = []
    
    if not ANTHROPIC_API_KEY:
        errors.append("ANTHROPIC_API_KEY not set")
    
    if not OPENAI_API_KEY:
        errors.append("OPENAI_API_KEY not set (needed for embeddings)")
    
    if errors:
        print("⚠️ Configuration warnings:")
        for error in errors:
            print(f"  - {error}")
        print("\nEdit .env file to add missing API keys")
        return False
    
    return True

if __name__ == "__main__":
    print("Configuration:")
    print(f"  BASE_DIR: {BASE_DIR}")
    print(f"  SEARXNG_URL: {SEARXNG_URL}")
    print(f"  CHROMADB_URL: {CHROMADB_URL}")
    print(f"  DEFAULT_MODEL: {DEFAULT_MODEL}")
    print(f"  MAX_SEARCH_RESULTS: {MAX_SEARCH_RESULTS}")
    print()
    validate_config()
