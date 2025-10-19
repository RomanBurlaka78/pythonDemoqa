import shutil
import tempfile

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()  # <-- исправлено

    # Check run in CI (GitHub Actions)
    is_ci = os.environ.get("CI") == "true"

    if is_ci:
        # === For CI ===
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        # uniq profile
        user_data_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    else:
        # === Local run ===
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--window-size=1400,1080")

    # Create driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    driver.quit()

    if is_ci:
        shutil.rmtree(user_data_dir, ignore_errors=True)


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
