#!/usr/bin/env python3
"""
Helper to store and retrieve content from ChromaDB
"""
import requests
import json
import sys
from typing import List, Dict
import hashlib

CHROMADB_URL = "http://localhost:8000/api/v1"

def store_content(collection: str, content: str, metadata: Dict, url: str = None):
    """Store content in ChromaDB"""
    # Create document ID from URL or content hash
    if url:
        doc_id = hashlib.md5(url.encode()).hexdigest()
    else:
        doc_id = hashlib.md5(content.encode()).hexdigest()
    
    payload = {
        "documents": [content],
        "metadatas": [metadata],
        "ids": [doc_id]
    }
    
    try:
        # Note: ChromaDB v2 API might differ, keeping v1 for now
        response = requests.post(
            f"{CHROMADB_URL}/collections/{collection}/add",
            json=payload
        )
        return {"success": True, "id": doc_id}
    except Exception as e:
        return {"success": False, "error": str(e)}

def search_content(collection: str, query: str, n_results: int = 5):
    """Search content in ChromaDB"""
    payload = {
        "query_texts": [query],
        "n_results": n_results
    }
    
    try:
        response = requests.post(
            f"{CHROMADB_URL}/collections/{collection}/query",
            json=payload
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    print("Storage helper loaded")
    print("Use: from storage_helper import store_content, search_content")
