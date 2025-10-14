from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver



class BasePage:
    URL = "https://demoqa.com/"

    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get(self.URL)
        return self

    def wait2(self):
        return WebDriverWait(self.driver, 2)

    def wait5(self):
        return WebDriverWait(self.driver, 5)

    def wait10(self):
        return WebDriverWait(self.driver, 10)

    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0,1000)")
        return self
