from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CareersPage(BasePage):
    """
    Page Object Model for Insider's Careers page.
    """

    LOCATIONS_BLOCK = (By.ID, "career-our-location")
    TEAMS_BLOCK = (By.ID, "career-find-our-calling")
    LIFE_AT_INSIDER_BLOCK = (By.CSS_SELECTOR, 'section[data-id="a8e7b90"]')

    def is_career_page_open(self):
        """
        Verify URL contains 'careers'.
        """
        return "careers" in self.driver.current_url.lower()

    def are_sections_visible(self):
        """
        Check visibility of major sections: Locations, Teams, Life at Insider.
        """
        return (
            self.is_displayed(self.LOCATIONS_BLOCK)
            and self.is_displayed(self.TEAMS_BLOCK)
            and self.is_displayed(self.LIFE_AT_INSIDER_BLOCK)
        )
