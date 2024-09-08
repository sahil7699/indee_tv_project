import pytest
from pytest_bdd import scenarios, given, when, then
from pages.book_hotels import HotelPage

# Load feature files
scenarios('features/hotel_booking.feature')

# Fixture for the HotelPage
@pytest.fixture
def hotel_page(driver):
    driver_instance, booking_type, no_of_people, url = driver
    return HotelPage(driver_instance, url, no_of_people)

# Step Definitions

@pytest.mark.skipif(
    lambda booking_type: booking_type != "hotel",
    reason="Skipping hotel tests as booking-type is not hotel"
)
@given('the user opens the Expedia website')
def open_expedia_website(hotel_page):
    hotel_page.open_url(hotel_page.url)

@when('the user selects "Hotels" and searches for hotels in "<location>"')
def search_hotels(hotel_page, location):
    hotel_page.search_hotel(location, hotel_page.no_of_people)

@when('the user picks the 2nd hotel from the search results')
def pick_second_hotel(hotel_page):
    hotel_page.select_second_hotel()

@then('extracts the room types and stores the room types in a JSON file')
def extract_room_types(hotel_page):
    result = hotel_page.extract_room_types()
    assert result, "Failed to store room types or no room types found."
