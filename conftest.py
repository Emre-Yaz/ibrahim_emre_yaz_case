import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.driver_factory import driver_factory


def pytest_addoption(parser):
    """
    Lets us set configs for our test run (desired browser, headless, etc.)

    Usage examples:
        pytest --headless
        pytest --browser=firefox
        pytest --browser=firefox --headless

    Defaults:
        browser: chrome
        headless: False (headed mode)
    """
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):
    """
    Shared fixture to initialize and teardown driver.

    Retrieves browser config from CLI flags set via pytest_addoption,
    creates the appropriate driver, and cleans up after test.

    Yields:
        Selenium WebDriver instance (Chrome or Firefox)
    """
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = driver_factory(browser=browser, headless=headless)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    If the test fails, it captures a screenshot and stores it 
    in the screenshots/ folder using the test function name.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")
