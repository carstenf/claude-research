.PHONY: help setup start stop restart logs test clean deploy

help:
	@echo "Trading Strategy Research System - Make Commands"
	@echo ""
	@echo "Development:"
	@echo "  make setup        - Initial setup (install deps, init db)"
	@echo "  make start        - Start Docker services"
	@echo "  make stop         - Stop Docker services"
	@echo "  make restart      - Restart Docker services"
	@echo "  make logs         - Show Docker logs"
	@echo "  make test         - Test services"
	@echo "  make clean        - Clean temporary files"
	@echo ""
	@echo "Production:"
	@echo "  make deploy       - Deploy full Docker stack"
	@echo "  make deploy-stop  - Stop production stack"

setup:
	@echo "🔧 Setting up system..."
	cp -n .env.example .env || true
	pip install --break-system-packages -r requirements.txt
	python3 scripts/init_db.py
	@echo "✅ Setup complete!"
	@echo "⚠️  Don't forget to edit .env with your API keys!"

start:
	@echo "🚀 Starting services..."
	docker-compose up -d
	@echo "✅ Services started!"
	@echo "   SearXNG:  http://localhost:8888"
	@echo "   ChromaDB: http://localhost:8000"

stop:
	@echo "⏹️  Stopping services..."
	docker-compose down
	@echo "✅ Services stopped"

restart:
	@echo "🔄 Restarting services..."
	docker-compose restart
	@echo "✅ Services restarted"

logs:
	docker-compose logs -f

test:
	@echo "🧪 Testing services..."
	@python3 scripts/researcher.py --test

clean:
	@echo "🧹 Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name ".DS_Store" -delete
	@echo "✅ Cleaned"

deploy:
	@echo "🚀 Deploying production stack..."
	docker-compose -f docker-compose.full.yml build
	docker-compose -f docker-compose.full.yml up -d
	@echo "✅ Production stack deployed!"

deploy-stop:
	@echo "⏹️  Stopping production stack..."
	docker-compose -f docker-compose.full.yml down
	@echo "✅ Production stack stopped"
