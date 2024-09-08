# Project Documentation

## Overview

This project automates the booking of flights and hotels using Selenium with Python. It includes:
- **Flight Booking**: Automates the search, sorting, selection, and booking of flights on Expedia.
- **Hotel Booking**: Automates the search and extraction of hotel room types on Expedia.
- **Testing**: Uses `pytest` and `pytest-bdd` to ensure the functionality of the booking processes through behavior-driven development (BDD).

## Project Structure

- **`pages/`**: Contains page object models for booking flights and hotels.
  - `book_flights.py`: Handles flight booking operations.
  - `book_hotels.py`: Handles hotel booking operations.
- **`tests/`**: Contains test cases and feature files.
  - `test_flight.py`: Contains tests for flight booking functionality.
  - `test_hotel.py`: Contains tests for hotel booking functionality.
  - `features/flight_booking.feature`: Feature file for flight booking tests.
  - `features/hotel_booking.feature`: Feature file for hotel booking tests.
- **`utils/`**: Contains utility classes and methods.
  - `elements.py`: Contains locators for flight and hotel booking elements.
  - `helper.py`: Contains helper methods for interacting with web elements.
- **`conftest.py`**: Configuration file for `pytest` fixtures and setup.
- **`room_details.json`**: JSON file where hotel room types are stored.

## Installation

- **Clone the Repository**
    ```sh
    git clone https://github.com/sahil7699/indee_tv_project.git
    cd <repository-directory>
    ```
- **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

## Feature Files

Feature files describe the behavior of the booking processes:

- **`features/flight_booking.feature`**: Contains scenarios for booking flights.
- **`features/hotel_booking.feature`**: Contains scenarios for booking hotels.

## Fixtures

Fixtures provide a way to set up and tear down test environments:

- **`driver`**: Initializes and configures the WebDriver.
- **`flight_page`**: Provides an instance of `FlightPage` for flight booking tests.
- **`hotel_page`**: Provides an instance of `HotelPage` for hotel booking tests.

## Page Object Models

- **`FlightPage`**: Handles operations related to flight booking. Methods include:
  - `search_flight`
  - `sort_results`
  - `select_cheapest_flight`
  - `proceed_to_checkout`
  - `enter_user_details`
  - `complete_booking_return_error`

- **`HotelPage`**: Handles operations related to hotel booking. Methods include:
  - `search_hotel`
  - `select_second_hotel`
  - `extract_room_types`

## Helper Functions

**`CommonOps`**: Provides common operations for web interactions:
- `open_url(url)`: Opens the given URL and maximizes the window.
- `find_element(locator)`: Finds a single element by locator.
- `find_elements(locator)`: Finds multiple elements by locator.
- `click(locator, return_text=False)`: Clicks on an element and optionally returns its text.
- `enter_text(locator, text, sleep_time=0)`: Enters text into an input field and optionally waits.
- `calculate_date(days_from_today)`: Calculates a future date based on the number of days from today.
- `close()`: Closes the WebDriver session.


## Running the Test Cases

To run the test cases, use the following commands:

1. **Flight Booking Tests**
    ```sh
    pytest tests/test_flight.py --booking-type flight
    ```

2. **Hotel Booking Tests**
    ```sh
    pytest tests/test_hotel.py --booking-type hotel
    ```