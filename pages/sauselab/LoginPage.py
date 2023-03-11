from selenium.webdriver.common.by import By
from lib.SeleniumHelper import SeleniumHelper

from lib.Logger import log_to_file
from config.TestConstants import TestConstants

class LoginPage(SeleniumHelper):

    url = TestConstants.URL
    username_txt = (By.ID, "user-name")
    password_txt = (By.ID, "password")
    login_btn = (By.NAME, "login-button")

    def __init__(self):
        super().__init__()
        log_to_file.info("Invoking url - {}".format(LoginPage.url))
        self.get_url(LoginPage.url)

    def click_login(self,username,password):
        log_to_file.info("Logging as username - {}".format(username))
        log_to_file.debug("Password - {}".format(password))
        self.send_keys(LoginPage.username_txt,username)
        self.send_keys(LoginPage.password_txt,password)
        self.click_on_element(LoginPage.login_btn)
        log_to_file.info("logging is successful...")

