import pytest

from pages.home_page import HomePage

name = "Ola"
@pytest.mark.regression
def test_text_box(driver):
    result: str = HomePage(driver)\
    .open() \
    .scroll_page() \
    .goto_elements_page \
    .go_to_text_box_page()\
    .fill_name(name)\
    .scroll_page()\
    .submit_data()\
    .check_result()

    assert result == f"Name:{name}"





