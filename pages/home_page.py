from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Page Object Model for Insider's Home Page.
    """

    # Locators
    COMPANY_MENU = (By.XPATH, '//a[normalize-space(text())="Company"]')
    CAREERS_LINK = (By.XPATH, '//a[text()="Careers"]')

    def __init__(self, driver):
        """
        Initialize HomePage with BasePage's driver.
        """
        super().__init__(driver)
        self.url = "https://www.useinsider.com/"

    def load(self):
        """Open the Insider homepage."""
        self.go_to(self.url)

    def is_title_correct(self):
        """Check if the homepage title contains 'Insider'."""
        return "Insider" in self.get_title()

    def open_careers_page(self):
        """
        Navigate to Careers page via Company > Careers menu.
        """
        self.hover_and_click(self.COMPANY_MENU, self.CAREERS_LINK)
