import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class QAJobsPage(BasePage):
    """
    Page Object Model for the Quality Assurance job listing page.
    """

    URL = "https://useinsider.com/careers/quality-assurance/"
    SEE_ALL_JOBS_BTN = (By.XPATH, '//a[contains(text(), "See all QA jobs")]')
    FILTER_LOCATION = (By.XPATH, '//select[@name="filter-by-location"]')
    FILTER_DEPARTMENT = (By.XPATH, '//select[@name="filter-by-department"]')
    JOB_CARDS = (By.CSS_SELECTOR, 'div.position-list-item')
    VIEW_ROLE_BTNS = (By.XPATH, '//a[contains(text(), "View Role")]')

    def load(self):
        """Go directly to QA page."""
        self.go_to(self.URL)

    def click_see_all_qa_jobs(self):
        """Click the button to list all QA jobs."""
        self.click(self.SEE_ALL_JOBS_BTN)

    def apply_filters(self, location: str, department: str):
        """
        Wait for filters to be visible, then apply them.
        """
        time.sleep(3)
        # Wait for dropdowns to be visible
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.FILTER_LOCATION)
        )
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.FILTER_DEPARTMENT)
        )

        # Wait for options inside the dropdowns to be visible
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: location in [o.text for o in Select(
                d.find_element(*self.FILTER_LOCATION)).options]
        )
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: department in [o.text for o in Select(
                d.find_element(*self.FILTER_DEPARTMENT)).options]
        )

        # Perform selection
        Select(self.find(self.FILTER_LOCATION)
               ).select_by_visible_text(location)
        Select(self.find(self.FILTER_DEPARTMENT)
               ).select_by_visible_text(department)

        time.sleep(3)

    def has_job_listings(self):
        """Return True if any job listings are found."""
        return len(self.find_all(self.JOB_CARDS)) > 0

    def all_positions_contain(self, text):
        """Verify all job titles contain given text."""
        job_titles = [card.find_element(
            By.TAG_NAME, "p").text for card in self.find_all(self.JOB_CARDS)]
        return all(text in title for title in job_titles)

    def all_departments_are(self, expected):
        """Check each job card shows the correct department."""
        departments = [
            card.find_elements(By.TAG_NAME, "span")[0].text for card in self.find_all(self.JOB_CARDS)
        ]
        return all(expected in dept for dept in departments)

    def all_locations_are(self, expected):
        """Check each job card shows the correct location."""
        locations = [
            card.find_elements(By.TAG_NAME, "div")[1].text for card in self.find_all(self.JOB_CARDS)
        ]
        return all(expected in loc for loc in locations)

    def click_first_view_role(self):
        """
        Hover over the first job card and click the 'View Role' button inside it using JS.
        Handles potential click interception by overlays or animations.
        """

        cards = self.find_all(self.JOB_CARDS)
        if not cards:
            raise Exception("No job cards found.")

        first_card = cards[0]

        # Hover over the card
        ActionChains(self.driver).move_to_element(first_card).perform()

        # Find the button within this card
        button = first_card.find_element(
            By.XPATH, './/a[contains(text(), "View Role")]')

        # Scroll to and click using JavaScript
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button)
        self.driver.execute_script("arguments[0].click();", button)

    def wait_load(self):
        """
        Wait until the QA jobs page is fully loaded by confirming
        that the 'Quality Assurance' filter is pre-selected.
        """
        selected_department_xpath = (
            '//span[@id="select2-filter-by-department-container" and @title="Quality Assurance"]'
        )

        locator = (By.XPATH, selected_department_xpath)

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
