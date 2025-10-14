from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage
from pages.elements.elements_page import ElementsPage
from pages.locators.locators_home_page import Locators
import allure


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.current_url
        return self


    def get_title(self):
        with allure.step("Get page title"):
            title = self.driver.title
            allure.attach(title,name="Page title: " + title, attachment_type=allure.attachment_type.TEXT)
            return title

    @property
    def goto_elements_page(self):
        with allure.step("Find elements page and click on it"):
            self.driver.find_element(By.XPATH, Locators.elements_page).click()
            return ElementsPage(self.driver)
