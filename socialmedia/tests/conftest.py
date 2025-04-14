
from typing import AsyncGenerator, Generator #type hinting with fixture
import pytest
from fastapi.testclient import TestClient #will allow to interact with API without having to start FastAPI server
from httpx import AsyncClient 

from socialmedia.main import app
from socialmedia.routers.post import comment_table, post_table

@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)

@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield

@pytest.fixture()
async def async_client(client) -> AsyncGenerator: #Dependency Injection
    async with AsyncClient(app=app, base_url=client.base_url) as ac:
        yield ac

