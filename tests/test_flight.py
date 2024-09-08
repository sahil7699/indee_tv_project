import pytest
from pytest_bdd import scenarios, given, when, then
from pages.book_flights import FlightPage

# Load feature files
scenarios('features/flight_booking.feature')

# Fixture for the FlightPage
@pytest.fixture
def flight_page(driver):
    driver, booking_type, no_of_people, url = driver
    return FlightPage(driver)

# Step Definitions
@pytest.mark.skipif(
    pytest.config.getoption("--booking-type") != "flight",
    reason="Skipping flight tests as booking-type is not flight"
)

@given('the user opens the Expedia website')
def open_expedia_website(flight_page):
    flight_page.driver.get(flight_page.url)
    flight_page.driver.maximize_window()

@when('the user selects "Flights" and chooses a one-way trip from "<source>" to "<dest>"')
def search_flights(flight_page, source, dest):
    flight_page.search_flight(source, dest, traveller=flight_page.no_of_people)

@when('the user sorts the results by "Duration (shortest)"')
def sort_results(flight_page):
    flight_page.sort_results()

@when('the user selects the cheapest flight available')
def select_cheapest_flight(flight_page):
    flight_page.select_cheapest_flight()

@when('the user proceeds to checkout')
def proceed_to_checkout(flight_page):
    flight_page.proceed_to_checkout()

@when('the user enters the following details: "<user_name>", "<user_surname>", "<user_email>", "<user_mobile>", "<user_street>", "<user_city>", "<user_zipcode>", "<user_pan>"')
def enter_user_details(flight_page, user_name, user_surname, user_email, user_mobile, user_street, user_city, user_zipcode, user_pan):
    flight_page.enter_user_details(user_name, user_surname, user_email, user_mobile, user_street, user_city, user_zipcode, user_pan)

@then('verifies the error message for missing credit card details')
def verify_error_message(flight_page):
    error_message = flight_page.complete_booking_return_error()
    assert "credit card" in error_message.lower(), "Error message for missing credit card details not found."

@then('captures the error text')
def capture_error_text(flight_page):
    error_message = flight_page.complete_booking_return_error()
    assert error_message, "No error message was captured."
