from pages.home_page import HomePage
from pages.careers_page import CareersPage


def test_screenshot_on_fail(driver):
    home = HomePage(driver)
    home.load()
    home.wait_for_page_load()
    assert home.is_homepage_open(), "Insider home page could not be opened."

    careers = CareersPage(driver)
    assert careers.is_career_page_open(), "Career page could not be opened."

    # Now that the test has failed, you can go /screenshots and see the screenshot.
