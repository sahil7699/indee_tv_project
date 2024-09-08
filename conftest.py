import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption("--booking-type", action="store", default="flight")
    parser.addoption("--no-of-people", action="store", default="1")
    parser.addoption("--url", action="store", default="https://www.expedia.co.in/")

@pytest.fixture
def driver(request):
    # Retrieve command-line options
    booking_type = request.config.getoption("--booking-type")
    no_of_people = int(request.config.getoption("--no-of-people"))
    url = request.config.getoption("--url")

    # Initialize WebDriver
    serv = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=serv)

    # Return driver and options for tests
    yield driver, booking_type, no_of_people, url
    driver.quit()

@pytest.fixture
def booking_type(request):
    return request.config.getoption("--booking-type")