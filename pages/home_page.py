from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object Model for Insider's Home Page.
    """

    # Locators
    COMPANY_MENU = (By.XPATH, '//a[normalize-space(text())="Company"]')
    CAREERS_LINK = (By.XPATH, '//a[text()="Careers"]')
    HOMEPAGE_SPECIFIER = (By.ID, 'home_logo_reel')

    def __init__(self, driver):
        """
        Initialize HomePage with BasePage's driver.
        """
        super().__init__(driver)
        self.url = "https://www.useinsider.com/"

    def load(self):
        """Open the Insider homepage."""
        self.go_to(self.url)

    def is_homepage_open(self):
        """
        Confirm the Insider homepage is loaded by checking:
        - The page title contains 'Insider'
        - The current URL includes useinsider.com
        - The homepage hero email input is visible
        """

        return (
            "Insider" in self.get_title() and
            "useinsider.com" in self.driver.current_url and
            self.is_displayed(self.HOMEPAGE_SPECIFIER)
        )

    def open_careers_page(self):
        """
        Navigate to Careers page via Company > Careers menu.
        """
        self.hover_and_click(self.COMPANY_MENU, self.CAREERS_LINK)
