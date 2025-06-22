from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    BasePage encapsulates common Selenium actions and utilities
    shared across all page objects in the framework.
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize the BasePage with driver and default timeout.

        Args:
            driver (WebDriver): Selenium WebDriver instance
            timeout (int): default wait timeout in seconds
        """
        self.driver = driver
        self.timeout = timeout

    def go_to(self, url):
        """Navigate to a URL."""
        self.driver.get(url)

    def get_title(self):
        """Return the current page title."""
        return self.driver.title

    def find(self, locator):
        """
        Wait for and return a visible element.

        Args:
            locator (tuple): (By.ID, 'id_value') or similar

        Returns:
            WebElement
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise Exception(
                f"Element with locator {locator} not visible after {self.timeout}s")

    def find_all(self, locator):
        """
        Return all matching elements.

        Args:
            locator (tuple): (By.CLASS_NAME, 'class_name') or similar

        Returns:
            list of WebElement
        """
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """Click a visible element."""
        self.find(locator).click()

    def is_displayed(self, locator):
        """Return True if element is visible."""
        try:
            return self.find(locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False

    def hover_and_click(self, menu_locator, link_locator):
        """
        Hover over one element to reveal another, then click the revealed element.

        Args:
            menu_locator (tuple): Locator for the element to hover over
            link_locator (tuple): Locator for the element revealed on hover
        """
        menu = self.find(menu_locator)

        ActionChains(self.driver).move_to_element(menu).perform()
        self.wait_until_visible(link_locator)
        self.click(link_locator)

    def wait_until_visible(self, locator):
        """
        Wait until a specific element is visible on the page.

        Args:
            locator (tuple): The locator of the element

        Returns:
            WebElement: The visible element
        """
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_page_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script(
                "return document.readyState") == "complete"
        )
        print("Page load completed")
