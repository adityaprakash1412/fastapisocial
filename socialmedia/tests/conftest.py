
from typing import AsyncGenerator, Generator #type hinting with fixture
import pytest
from fastapi.testclient import TestClient #will allow to interact with API without having to start FastAPI server
from httpx import AsyncClient 

from socialmedia.main import app
from socialmedia.routers.post import comment_table, post_table

