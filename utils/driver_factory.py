from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def driver_factory(browser: str = "chrome", headless: bool = False):
    """
    Driver factory to create browser instances for Selenium.

    Args:
        browser (str): "chrome" or "firefox"
        headless (bool): If True, runs browser in headless mode

    Returns:
        Selenium WebDriver instance

    Raises:
        ValueError: If unsupported browser is specified
    """
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        return webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")
