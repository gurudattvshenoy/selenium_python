from selenium.webdriver.common.by import By
from lib.SeleniumHelper import SeleniumHelper

from lib.Logger import log_to_file

class InventoryPage(SeleniumHelper):

    app_logo_txt = (By.XPATH, '//div[@class="app_logo"]')
    hamburger_menu =(By.ID,'react-burger-menu-btn')
    logout_lnk =(By.ID,"logout_sidebar_link")

    def __init__(self):
        super().__init__()

    def get_app_logo_text(self):
        text = self.get_text(InventoryPage.app_logo_txt)
        log_to_file.info("App logo text is - {}".format(text))
        return text

    def click_on_hamburger_menu(self):
        log_to_file.info("Clicking on hamburger menu")
        self.click_on_element(InventoryPage.hamburger_menu)

    def click_on_logout(self):
        log_to_file.info("Clicking on logout...")
        self.click_on_element(InventoryPage.logout_lnk)

