# Validation Status:
# - Security Validation: Nestor [2025-04-24] ✅
# - Strategic Validation: Pulse [2025-04-24] ✅
# - Governance Validation: Agent-47 [2025-04-24] ✅


install:
	@echo "🔧 Installing logdoc in editable mode..."
	@if [ ! -f pyproject.toml ]; then echo "❌ pyproject.toml not found"; exit 1; fi
	@pip install -e .
	@echo "✅ Installed logdoc CLI"

check-env:
	@echo "🧪 Checking Python environment..."
	@if [ -z "$$VIRTUAL_ENV" ]; then \
	  echo "⚠️  Warning: No virtual environment detected"; \
	else \
	  echo "✅ Virtual environment active: $$VIRTUAL_ENV"; \
	fi

test:
	@echo "🧪 Running tests with pytest..."
	@pytest tests || echo "⚠️  Some tests failed."

lint:
	@echo "🔍 Linting with flake8..."
	@flake8 src || echo "⚠️  Linting issues detected."

format:
	@echo "🎨 Formatting code with black..."
	@black src

clean:
	@echo "🧹 Cleaning temporary files..."
	@find . -type d -name '__pycache__' -exec rm -r {} +
	@find . -type f -name '*.pyc' -delete
	@rm -rf *.egg-info

link:
	@echo "🔗 Linking logdoc to ../scannest-ml via CLI..."
	@python src/logdoc/cli.py ../scannest-ml --mode copy --inject

inject:
	@echo "🪛 Injecting headers into ../scannest-ml/src..."
	@python src/logdoc/cli.py ../scannest-ml --inject

unlink:
	@echo "🧼 Removing deployed logdoc from ../scannest-ml/src/logdoc"
	@rm -rf ../scannest-ml/src/logdoc

freeze:
	@echo "📦 Generating requirements.txt from requirements.in..."
	@pip install pip-tools >/dev/null 2>&1 || echo "⚠️ pip-tools not installed"
	@pip-compile requirements.in -o requirements.txt || echo "❌ requirements.in missing?"

help:
	@echo "Available commands:"
	@echo "  make install        Install logdoc CLI in editable mode"
	@echo "  make check-env      Check if virtualenv or conda is active"
	@echo "  make test           Run pytest in ./tests"
	@echo "  make lint           Lint Python code in ./src"
	@echo "  make format         Format Python code with black"
	@echo "  make clean          Remove .pyc, __pycache__, egg-info"
	@echo "  make link           Copy and inject logdoc into ../scannest-ml"
	@echo "  make inject         Inject headers only into ../scannest-ml"
	@echo "  make unlink         Remove deployed logdoc from ../scannest-ml"
	@echo "  make freeze         Generate requirements.txt from requirements.in"
	@echo "  make help           Show this help message"
