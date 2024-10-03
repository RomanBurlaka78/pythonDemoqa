from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.locators.locators_home_page import Locators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def goto_elements_page(self):
        self.driver.find_element(By.XPATH, Locators.elements_page).click()
