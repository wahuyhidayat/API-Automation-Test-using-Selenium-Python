import pytest
import uuid
from api.user_api import UserAPI

@pytest.fixture
def user_data():
    unique_email = f"prabowo.s.{uuid.uuid4()}@gmail.com"
    return {
        "name": "Prabowo Subianto",
        "email": unique_email,
        "gender": "male",
        "status": "active"
    }

@pytest.fixture
def invalid_user_data():
    return {
        "name": "Jusuf Kalla",
        "email": "invaild.gmail.com",
        "gender": "unknown",
        "status": "undefined"
    }

@pytest.fixture
def blank_user_data():
    return {
        "name": "",
        "email": "",
        "gender": "",
        "status": ""
    }


@pytest.fixture
def updated_data():
    return {
        "name": "Joko Widodo"
    }

@pytest.fixture
def created_user(user_data):
    response = UserAPI.create_user(user_data)
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    yield response
