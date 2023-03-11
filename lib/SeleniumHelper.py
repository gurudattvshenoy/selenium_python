from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from lib.Logger import log_to_file
from lib.SeleniumDriverManager import SeleniumDriverManager

class SeleniumHelper(SeleniumDriverManager):

    def __init__(self):
        log_to_file.debug("Inside SeleniumHelper constructor...")
        super().__init__()

    def get_url(self,url):
        log_to_file.debug("Getting url -{}".format(url))
        self.driver.get(url)

    def get_webelement(self,webelement):
        try:
            log_to_file.debug("Getting webelement - {}".format(webelement))
            return self.driver_wait.until(EC.element_to_be_clickable(webelement))
        except Exception as ex:
            log_to_file.error("Exception occured while finding element {} - {}".format(webelement[1],str(ex)))
            raise ex

    def get_webelements(self,webelement):
        try:
            log_to_file.debug("Getting webelement - {}".format(webelement))
            return self.driver.find_elements(*webelement)
        except Exception as ex:
            log_to_file.error("Exception occured while finding elements {} - {}".format(webelement[1],str(ex)))
            raise ex

    def get_text(self, webelement):
        log_to_file.debug("Getting text for webelement - {}".format(webelement))
        return self.get_webelement(webelement).text

    def send_keys(self,webelement,value):
        log_to_file.debug("Sending values to {} webelement - {}".format(value,webelement))
        self.get_webelement(webelement).send_keys(value)

    def click_on_element(self, webelement):
        log_to_file.debug("Clicking on webelement - {}".format(webelement))
        self.get_webelement(webelement).click()

    def submit(self,webelement):
        log_to_file.debug("Clicking on submit on webelement - {}".format(webelement))
        self.get_webelement(webelement).submit()

    def refresh_page(self):
        log_to_file.debug("Refreshing page...")
        self.driver.refresh()

    def get_page_title(self):
        title = self.driver.title
        log_to_file.debug("Got page title - {}".format(title))
        return title

    def get_current_url(self):
        current_url = self.driver.current_url
        log_to_file.debug("Current url - {}".format(current_url))
        return current_url

    def select_drop_down_by_visible_text(self,webelement, text):
        log_to_file.debug("Attempting to select dropdown - {} using visible text - {}".format(webelement,text))
        s = Select(self.get_webelement(webelement))
        s.select_by_visible_text(text)
        log_to_file.debug("Drop-down selection by visible text is successful..")

    def select_drop_down_by_index(self,webelement, index):
        log_to_file.debug("Attempting to select dropdown - {} using index number - {}".format(webelement, index))
        s = Select(self.get_webelement(webelement))
        s.select_by_index(index)
        log_to_file.debug("Drop-down selection using index is successful..")

    def select_drop_down_by_value(self, webelement, value):
        log_to_file.debug("Attempting to select dropdown - {} using value attribute - {}".format(webelement, value))
        s = Select(self.get_webelement(webelement))
        s.select_by_value(value)
        log_to_file.debug("Drop-down selection by value is successful..")

    def accept_alert(self):
        log_to_file.debug("Attempting to accept alert window ")
        self.driver.switch_to.alert.accept()
        log_to_file.debug("Alert is accepted...")

    def get_alert_text(self):
        log_to_file.debug("Fetching alert text is successful..")
        alert_text =  self.driver.switch_to.alert.text
        log_to_file.debug("Got alert text - {}".format(alert_text))
        return alert_text

    def dismiss_alert(self):
        log_to_file.debug("Dismissing alert...")
        self.driver.switch_to.alert.dismiss()

    def move_mouse_over(self,elem):
        action = ActionChains(self.driver)
        return action.move_to_element(elem)

    def action_chain_perform_click(self, action):
        action.click().perform()

    def go_forward(self):
        log_to_file.debug("Clicking on forward button on browser")
        self.driver.forward()

    def go_back(self):
        log_to_file.debug("Clicking on back button on browser")
        self.driver.back()

    def maximize_window(self):
        log_to_file.debug("Maximizing the browser window...")
        self.driver.maximize_window()

    def close_window(self):
        log_to_file.debug("Closing current browser window...")
        self.driver.close()

    def quit_driver(self):
        log_to_file.debug("Closing driver i.e. all opened windows...")
        self.driver.quit()


