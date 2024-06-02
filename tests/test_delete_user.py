import pytest
from api.user_api import UserAPI
from config import INVALID_ID

def test_delete_user_with_valid_id(created_user):
    user_id = created_user.json().get("id")
    response = UserAPI.delete_user(user_id)
    if response.status_code == 204:
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"
    else:
        assert response.json()[0].get("message") == "Table minimum records limit reached, please add some records", f"Unexpected error message: {response.json()}"

def test_delete_user_invalid_id():
    response = UserAPI.delete_user(INVALID_ID)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_delete_user_by_name(created_user):
    user_name = created_user.json().get("name")
    response = UserAPI.delete_user(user_name)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_delete_user_without_id(created_user):
    user_id = created_user.json().get("")
    response = UserAPI.delete_user(user_id)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"
    
def test_delete_user_without_token(created_user):
    user_id = created_user.json().get("id")
    response = UserAPI.delete_user_without_token(user_id)
    assert response.status_code == 404, f"Expected status code 404, but got {response.status_code}"

def test_delete_user_with_invalid_token(created_user):
    user_id = created_user.json().get("id")
    response = UserAPI.delete_user_with_invalid_token(user_id)
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"