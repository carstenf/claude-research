#!/usr/bin/env python3
"""
Quick test of the research system components
"""

import chromadb
from anthropic import Anthropic
import os

print("🧪 Testing Research System Components...")

# Test 1: ChromaDB
print("\n1️⃣ Testing ChromaDB...")
try:
    client = chromadb.Client()
    collection = client.create_collection("test")
    collection.add(
        documents=["This is a test document"],
        ids=["test1"]
    )
    results = collection.query(query_texts=["test"], n_results=1)
    print("   ✅ ChromaDB working!")
except Exception as e:
    print(f"   ❌ ChromaDB error: {e}")

# Test 2: Anthropic API
print("\n2️⃣ Testing Anthropic API...")
try:
    # Check if API key exists
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("   ⚠️  ANTHROPIC_API_KEY not set in environment")
        print("   ℹ️  Add it to .env file")
    else:
        client = Anthropic()
        print("   ✅ Anthropic client initialized!")
except Exception as e:
    print(f"   ❌ Anthropic error: {e}")

print("\n✨ System ready for research tasks!")
print("\n📋 Next steps:")
print("   1. Add ANTHROPIC_API_KEY to .env file")
print("   2. Start with Iron Condor analysis")
print("   3. Docker services optional for now")
