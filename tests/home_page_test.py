from pages.elements.elements_page import ElementsPage
from pages.home_page import HomePage
from conftest import driver


def test_get_url(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.get_title


def test_goto_elements_page(driver):
    home_page = HomePage(driver)
    home_page.open()
    home_page.scroll_page()
    home_page.goto_elements_page()
    elements_page = ElementsPage(driver)
    elements_page.get_title()

    assert elements_page.get_title() == "DEMOQA"
    assert elements_page.get_title().__eq__("DEMOQA")
