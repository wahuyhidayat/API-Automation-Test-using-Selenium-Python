import pytest
from api.user_api import UserAPI
from config import INVALID_ID

def test_get_user_by_id(created_user):
    user_id = created_user.json().get("id")
    response = UserAPI.get_user(user_id)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_get_user_by_name(created_user):
    user_name = created_user.json().get("name")
    response = UserAPI.get_user(user_name)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_get_user_by_email(created_user):
    user_email = created_user.json().get("email")
    response = UserAPI.get_user(user_email)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_get_user_by_gender(created_user):
    user_gender = created_user.json().get("gender")
    response = UserAPI.get_user(user_gender)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_get_user_by_status(created_user):
    user_status = created_user.json().get("status")
    response = UserAPI.get_user(user_status)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_get_user_with_invalid_id():
    response = UserAPI.get_user(INVALID_ID)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_get_user_without_parameter():
    response = UserAPI.get_user("")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

def test_get_user_with_invalid_parameter():
    response = UserAPI.get_user("1@!3$7&")
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_get_user_with_invalid_token(created_user):
    user_id = created_user.json().get("id")
    response = UserAPI.get_user_with_invalid_token(user_id)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
