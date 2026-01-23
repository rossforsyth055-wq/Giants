"""FastAPI application entry point."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Giants Personal Training", version="0.1.0")

# Setup paths
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Setup templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get("/", response_class=HTMLResponse, name="home")
async def home(request: Request) -> HTMLResponse:
    """Home page."""
    return templates.TemplateResponse(request, "home.html")


@app.get("/booking", response_class=HTMLResponse, name="booking")
async def booking(request: Request) -> HTMLResponse:
    """Class booking page."""
    return templates.TemplateResponse(request, "booking.html")


@app.get("/recipes", response_class=HTMLResponse, name="recipes")
async def recipes(request: Request) -> HTMLResponse:
    """Recipes page."""
    return templates.TemplateResponse(request, "recipes.html")


@app.get("/video", response_class=HTMLResponse, name="video")
async def video(request: Request) -> HTMLResponse:
    """Video training subscription page."""
    return templates.TemplateResponse(request, "video.html")


@app.get("/wellness", response_class=HTMLResponse, name="wellness")
async def wellness(request: Request) -> HTMLResponse:
    """Giant Wellness treatments page."""
    return templates.TemplateResponse(request, "wellness.html")


@app.get("/health")
async def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
