from selenium.webdriver.common.by import By

from pages.base.base_page import BasePage
from pages.elements.text_box_page import TextBoxPage
from pages.locators.locators_elements_page import LocatorsElementsPage


class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



    def get_title(self):
        return self.driver.title

    def go_to_text_box_page(self):
       self.driver.find_element(By.XPATH, LocatorsElementsPage.text_box_link).click()

       return TextBoxPage(self.driver)