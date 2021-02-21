import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="enter language")


@pytest.fixture(scope="function")
def browser():
    print("\nStarting firefox...")
    browser = webdriver.Firefox()
    yield browser
    print("\n closing browser...")
    browser.quit()


@pytest.fixture(scope="function")
def user_language(request):
    user_language = request.config.getoption("language")
    return user_language

