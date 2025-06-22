from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage


def test_qa_job_redirection(driver):
    # Step 1: Go to homepage
    home = HomePage(driver)
    home.load()
    home.wait_for_page_load()
    assert home.is_homepage_open(), "Insider home page could not be opened."

    # Step 2: Navigate to Careers via Company menu
    home.open_careers_page()

    careers = CareersPage(driver)
    careers.wait_for_page_load()
    assert careers.is_career_page_open(), "Career page could not be opened."
    assert careers.are_sections_visible(
    ), "Career page sections (Locations, Teams, Life at Insider) not visible"

    # Step 3: Go directly to QA page and filter jobs
    qa_jobs = QAJobsPage(driver)
    qa_jobs.load()
    qa_jobs.click_see_all_qa_jobs()
    qa_jobs.wait_for_page_load()
    qa_jobs.apply_filters(location="Istanbul, Turkiye",
                          department="Quality Assurance")

    # Step 4: Validate filtered job results
    assert qa_jobs.has_job_listings(), "No QA job listings found after filtering"
    assert qa_jobs.all_positions_contain(
        "Quality Assurance"), "Some job titles do not contain 'Quality Assurance'"
    assert qa_jobs.all_departments_are(
        "Quality Assurance"), "Some jobs are not in 'Quality Assurance' department"
    assert qa_jobs.all_locations_are(
        "Istanbul, Turkiye"), "Some job locations are not 'Istanbul, Turkiye'"

    # Step 5: Redirect to application form
    qa_jobs.click_first_view_role()

    # Switch to Lever tab
    driver.switch_to.window(driver.window_handles[-1])
    assert "lever.co" in driver.current_url, "Redirection to Lever application page was not successful"
