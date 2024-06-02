import pytest
from api.user_api import UserAPI
from config import INVALID_ID

def test_put_user_with_valid_id(created_user, updated_data):
    user_id = created_user.json().get("id")
    response = UserAPI.update_user(user_id, updated_data)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.json().get("name") == "Joko Widodo", "User name was not updated"

def test_put_user_with_invalid_id(updated_data):
    response = UserAPI.update_user(INVALID_ID, updated_data)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_put_user_with_invalid_data(created_user, invalid_user_data):
    user_id = created_user.json().get("id")
    response = UserAPI.update_user(user_id, invalid_user_data)
    assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"

def test_put_user_with_invalid_id_and_data(invalid_user_data):
    response = UserAPI.update_user(INVALID_ID, invalid_user_data)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_put_user_with_invalid_id_and_valid_data(updated_data):
    response = UserAPI.update_user(INVALID_ID, updated_data)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_put_user_without_id(created_user, updated_data):
    user_id = created_user.json().get("")
    response = UserAPI.update_user_without_token(user_id, updated_data)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_put_user_without_token(created_user, updated_data):
    user_id = created_user.json().get("id")
    response = UserAPI.update_user_without_token(user_id, updated_data)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_put_user_with_invalid_token(created_user, updated_data):
    user_id = created_user.json().get("id")
    response = UserAPI.update_user_with_invalid_token(user_id, updated_data)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
