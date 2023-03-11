from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from lib.Logger import log_to_file
from config.TestConstants import TestConstants
class SeleniumDriverManager:

    browser = TestConstants.BROWSER

    def __init__(self):
        log_to_file.debug("Inside Selenium driver manager...")
        self._driver = None

    @property
    def driver(self):
        if self._driver is None:
            if SeleniumDriverManager.browser == "chrome":
                log_to_file.debug("Initializing chrome browser...")
                self._driver = Chrome(service=Service(ChromeDriverManager().install()))
                self._driver.implicitly_wait(TestConstants.IMPLICIT_TIMEOUT)

            elif SeleniumDriverManager.browser == "firefox":
                log_to_file.debug("Initializing firefox browser...")
                self._driver = Firefox(service=Service(GeckoDriverManager().install()))
            else:
                log_to_file.debug("Initializing of chrome or firefox browser failed...")
                raise AttributeError("Unsupported browser: {}".format(SeleniumDriverManager.browser))
        return self._driver


    @property
    def driver_wait(self):
        log_to_file.debug("Initializing webdriver wait...")
        self._driver_wait = WebDriverWait(self.driver, TestConstants.EXPLICIT_TIMEOUT)
        return self._driver_wait



