"""Tests for the main API."""

from __future__ import annotations

from httpx import ASGITransport, AsyncClient

from giants.main import app


async def test_home_page() -> None:
    """Test the home page returns HTML."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Giants Personal Training" in response.text


async def test_booking_page() -> None:
    """Test the booking page returns HTML."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/booking")
    assert response.status_code == 200
    assert "Class Booking" in response.text


async def test_recipes_page() -> None:
    """Test the recipes page returns HTML."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/recipes")
    assert response.status_code == 200
    assert "Healthy Recipes" in response.text


async def test_video_page() -> None:
    """Test the video training page returns HTML."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/video")
    assert response.status_code == 200
    assert "Video Training" in response.text


async def test_wellness_page() -> None:
    """Test the wellness page returns HTML."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/wellness")
    assert response.status_code == 200
    assert "Giant Wellness" in response.text


async def test_health_endpoint() -> None:
    """Test the health check endpoint returns ok status."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
