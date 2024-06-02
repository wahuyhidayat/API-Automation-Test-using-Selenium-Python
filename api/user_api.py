import requests
from config import BASE_URL, HEADERS, INVALID_HEADERS

class UserAPI:

    @classmethod
    def create_user(cls, user_data):
        response = requests.post(f"{BASE_URL}/users", json=user_data, headers=HEADERS)
        return response

    @classmethod
    def create_user_without_token(cls, user_data):
        response = requests.post(f"{BASE_URL}/users", json=user_data)
        return response

    @classmethod
    def create_user_with_invalid_token(cls, user_data):
        response = requests.post(f"{BASE_URL}/users", json=user_data, headers=INVALID_HEADERS)
        return response

    @classmethod
    def get_user(cls, user_id):
        response = requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
        return response

    @classmethod
    def get_user_with_invalid_token(cls, user_id):
        response = requests.get(f"{BASE_URL}/users/{user_id}", headers=INVALID_HEADERS)
        return response
        
    @classmethod
    def update_user(cls, user_id, updated_data):
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data, headers=HEADERS)
        return response

    @classmethod
    def update_user_without_token(cls, user_id, updated_data):
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)
        return response

    @classmethod
    def update_user_with_invalid_token(cls, user_id, updated_data):
        response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data, headers=INVALID_HEADERS)
        return response

    @classmethod
    def delete_user(cls, user_id):
        response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
        if response.status_code != 204:
            try:
                response_json = response.json()
                if isinstance(response_json, list) and response_json:
                    if response_json[0].get("message") == "Table minimum records limit reached, please add some records":
                        print(f"Cannot delete user: {response_json[0].get('message')}")
                else:
                    print(f"Failed to delete user. Status code: {response.status_code}, Response: {response_json}")
            except (KeyError, IndexError, ValueError) as e:
                print(f"Unexpected error format or content: {e}, Response: {response.text}")
        return response
    
    @classmethod
    def delete_user_without_token(cls, user_id):
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        return response
    
    @classmethod
    def delete_user_with_invalid_token(cls, user_id):
        response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=INVALID_HEADERS)
        return response
    