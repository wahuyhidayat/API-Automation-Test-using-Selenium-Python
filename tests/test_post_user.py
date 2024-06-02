import pytest
from api.user_api import UserAPI

def test_post_user_with_valid_data(created_user):
    response = created_user
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert "id" in response.json(), "Expected 'id' in response json"

def test_post_user_with_invalid_data(invalid_user_data):
    response = UserAPI.create_user(invalid_user_data)
    assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"

def test_post_user_with_blank_data(blank_user_data):
    response = UserAPI.create_user(blank_user_data)
    assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"

def test_post_user_without_request_body():
    response = UserAPI.create_user({})
    assert response.status_code == 422, f"Expected status code 422, but got {response.status_code}"

def test_post_user_without_token(user_data):
    response = UserAPI.create_user_without_token(user_data)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"

def test_post_user_with_invalid_token(user_data):
    response = UserAPI.create_user_with_invalid_token(user_data)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
