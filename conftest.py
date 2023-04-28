import pytest
from selene import browser


@pytest.fixture
def browser_configuration():
    browser.browser_name = "chrome"
    browser.window_height = 1080
    browser.window_width = 720
