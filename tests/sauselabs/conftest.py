import pytest
from lib.SeleniumDriverManager import SeleniumDriverManager
from pages.sauselab.SauceLabs import SauceLabs

@pytest.fixture(scope="module")
def saucelabs_helper():
    SeleniumDriverManager.browser = "chrome"
    sauceLabs = SauceLabs()
    sauceLabs.get_url("https://www.saucedemo.com/")
    sauceLabs.maximize_window()
    yield sauceLabs
    print("cleaning up")
    sauceLabs.click_on_hamburger_menu()
    sauceLabs.click_on_logout()
    sauceLabs.close_window()

