import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size = 1400, 1080")
    service_properties = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_properties, options=chrome_options)

    yield driver

    driver.quit()
