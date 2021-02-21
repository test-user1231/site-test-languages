import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="enter language")
    parser.addoption('--browser', action='store', default=None, help="select browser")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "firefox":
        print("starting firefox...")
        browser = webdriver.Firefox()
    elif browser_name == "chrome":
        print("starting chrome...")
        browser = webdriver.Chrome()
    else:
        print("not found name for browser")

    yield browser
    print("closing browser ")
    browser.quit()


@pytest.fixture(scope="function")
def user_language(request):
    user_language = request.config.getoption("language")
    return user_language

