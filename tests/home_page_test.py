from pages.elements.elements_page import ElementsPage
from pages.home_page import HomePage
from conftest import driver
import allure


@allure.epic("Demoqa")
@allure.feature("Elements")
@allure.story("Homepage")
def test_get_url(driver):
    home_page = HomePage(driver)
    home_page.open()\
    .get_title()


def test_goto_elements_page(driver):
    title = HomePage(driver)\
    .open()\
    .scroll_page()\
    .goto_elements_page\
    .get_title()

    assert title.__eq__("DEMOQA")
