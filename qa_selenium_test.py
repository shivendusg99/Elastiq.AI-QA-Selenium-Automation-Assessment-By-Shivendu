import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()  # Replace with your desired browser
    yield driver
    driver.quit()

def test_search_functionality(driver):
    # Navigate to the Selenium Playground Table Search Demo
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo.html")

    # Locate and interact with the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
    )
    search_box.send_keys("New York")

    # Validate the search results
    results_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="dataTables_info"]'))
    ).text
    assert "Showing 5 entries out of 24 total entries" in results_text
