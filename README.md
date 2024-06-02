# API Automation Testing
This project implements automated testing for APIs using Python and pytest. It includes various test scenarios for HTTP methods like GET, POST, PUT, and DELETE on API endpoints hosted at [Go REST](https://gorest.co.in/).

## Getting Started
To enjoy the automated tests, develop the framework or adapt it to your own purpose, just download the project or clone repository.
Here are the things that need to be prepared before conducting testing:
1. Download and install [python](https://www.python.org/downloads/)
2. Install [pip](https://pypi.org/project/pip/)
3. Install [selenium](https://pypi.org/project/selenium/)
4. Install [pytest](https://pypi.org/project/pytest/)
5. Install [request](https://pypi.org/project/requests/)
6. Install [pytest-html](https://pypi.org/project/pytest-html/)

## Project Structure
Here you can find a short description of the main directories and it's content.
- [api/user_api.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/api/user_api.py): Contains the UserAPI class with methods for creating, reading, updating, and deleting users.
- [tests/conftest.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/tests/conftest.py): Contains pytest fixtures used to set up testing data.
- [tests/test_get_user.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/tests/test_get_user.py): Contains the main testing scenarios for HTTP methods.
- [tests/test_post_user.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/tests/test_post_user.py): Contains the main testing scenarios for HTTP POST methods.
- [tests/test_put_user.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/tests/test_put_user.py): Contains the main testing scenarios for HTTP PUT methods.
- [tests/test_delete_user.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/tests/test_delete_user.py): Contains the main testing scenarios for HTTP DELETE methods.
- [config.py](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/config.py): Contains basic configuration such as API base URL and authentication token.
- [pytest.ini](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/pytest.ini): Contains pytest configuration for automatically generating HTML reports after testing completes.

## Run Test
To run the tests, simply use the following command:
```bash
pytest -v
```
## Test Result
The testing will automatically generate a report in HTML format saved as [report_api_automation.html](https://github.com/wahuyhidayat/API-Automation-Test-using-Selenium-Python/blob/main/report_api_automation.html). You can open this report in a browser to view detailed test results.
