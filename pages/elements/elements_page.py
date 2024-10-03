from pages.base_page import BasePage


class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        return self.driver.title
