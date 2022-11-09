import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
     parser.addoption('--language', action='store', default='en',
                      help="Choose language from list")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print('\nstart browser')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(20)
    #raise pytest.UsageError(f"--language should be from list")
    yield browser
    print('\nquit browser..')
    browser.quit()

