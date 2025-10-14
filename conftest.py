
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    # === BEFORE test ===
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size = 1400, 1080")
    service_properties = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service_properties, options=chrome_options)

    yield driver

    driver.quit()

 # === AFTER test ===
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome_ = yield
    report = outcome_.get_result()

    if report.when == "call":
        item.rep_call = report
        if report.passed:
            print(f"\nTest {item.name}:  PASSED")
        elif report.failed:
            print(f"\nTest {item.name}: FAILED: {report.longrepr}")
        elif report.skipped:
            print(f"\nTest {item.name}: SKIPPED")
