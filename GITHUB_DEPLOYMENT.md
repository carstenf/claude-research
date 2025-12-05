# GitHub Deployment Guide

## When the system is stable and tested

### 1. Initialize Git Repository

```bash
cd /home/carsten/research

# Initialize git
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: Trading Strategy Research System"
```

### 2. Create GitHub Repository

```bash
# On GitHub: Create new repository "trading-research-system"
# Private or Public (recommend: Private)

# Add remote
git remote add origin git@github.com:YOUR_USERNAME/trading-research-system.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Setup GitHub Actions (Optional)

Create `.github/workflows/docker-build.yml`:

```yaml
name: Docker Build

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build Docker image
        run: docker build -f Dockerfile.production -t research-agent:latest .
      - name: Test image
        run: |
          docker run --rm research-agent:latest python -c "import requests; print('OK')"
```

### 4. Documentation

Add to GitHub:
- README.md (already created)
- ARCHITECTURE.md (detailed architecture)
- API.md (API documentation when implemented)
- CONTRIBUTING.md (contribution guidelines)

### 5. Deployment from GitHub

On any new server:

```bash
# Clone repository
git clone git@github.com:YOUR_USERNAME/trading-research-system.git
cd trading-research-system

# Setup environment
cp .env.example .env
nano .env  # Add API keys

# Deploy
docker-compose -f docker-compose.full.yml up -d
```

### 6. Keep Private Data Secure

Files in .gitignore (NOT in GitHub):
- .env (API keys)
- domains/ (research data)
- chroma_data/ (vector database)
- reports/ (generated reports)
- *.db (SQLite databases)

Only code and configuration templates go to GitHub!

---

**Status:** 📝 Ready to deploy when stable  
**Next:** Test system thoroughly before pushing to GitHub
