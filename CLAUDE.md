# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies (use a virtual environment)
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Run the development server
uvicorn giants.main:app --reload

# Run all tests
pytest

# Run a single test file
pytest tests/test_main.py

# Run a specific test
pytest tests/test_main.py::test_root -v

# Linting and formatting
ruff check .
ruff format .

# Type checking
mypy src/
```

## Architecture

- **src/giants/main.py** - FastAPI application entry point, contains the `app` instance
- **src/giants/** - Main application package
- **tests/** - Pytest test files using httpx AsyncClient for API testing
