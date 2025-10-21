import allure

from conftest import driver
from pages.base.base_page import BasePage
from pages.locators.locators_text_box_page import LocatorsTextBox
from selenium.webdriver.common.by import By

class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_name(self, name):
        with allure.step("Fill name"):
            self.driver.find_element(By.ID,LocatorsTextBox.user_name).send_keys(name)
            allure.attach(name, name="Fill name : " + name, attachment_type=allure.attachment_type.TEXT)
            return self

    def submit_data(self):
        self.driver.find_element(By.ID, LocatorsTextBox.btn_submit).click()
        return self

    def check_result(self):
        self.driver.implicitly_wait(6)
        get_text_name = self.driver.find_element(By.ID, LocatorsTextBox.name).text

        return get_text_name



