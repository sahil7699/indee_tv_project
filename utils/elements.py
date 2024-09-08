from selenium.webdriver.common.by import By

class CommonElements:
    date_tab = (By.XPATH,"//button[@data-testid='uitk-date-selector-input1-default']")
    date = [By.XPATH,"//div[@class='uitk-day-button uitk-day-selectable uitk-day-clickable' and ./div[contains(@aria-label,'ADD DATE HERE')]]"]
    done_btn = (By.XPATH,"//button[text()='Done']")
    travellers_btn = (By.XPATH,"//label[@class='uitk-field-label' and text()='Travellers' ]/following-sibling::button")
    search_btn = (By.XPATH,"//button[@id='search_button']")

class FlightBookingElements(CommonElements):
    
    # main page
    flight_tab = (By.XPATH,"//a[@class='uitk-tab-anchor' and span[text()='Flights']]")
    one_way = (By.XPATH,"//a[@class='uitk-tab-anchor' and span[text()='One-way']]")
    source_btn = (By.XPATH,"//button[@aria-label='Leaving from']")
    source_input = (By.XPATH,"//section[@data-testid='popover-sheet']//input[@id='origin_select']")
    dest_btn = (By.XPATH,"//button[@aria-label='Going to']")
    dest_input = (By.XPATH,"//section[@data-testid='popover-sheet']//input[@id='destination_select']")
    increase_traveller = (By.XPATH,"//*[@aria-label='Increase the number of adults']")
        
    # search result page
    flight_list = (By.XPATH,"//ul[@data-test-id='listings']")
    shortest_duration = (By.XPATH,"//select[@id='sort-filter-dropdown-SORT']/option[@value='DURATION_INCREASING']")
    select_shortest_cheapest_flight = (By.XPATH , "//ul[@data-test-id='listings']/li[1]")
    details_and_fare_page = (By.XPATH,"//div[@data-test-id='details-and-fares']")
    select_button = (By.XPATH,"//button[@data-test-id='select-button']")
    checkout_button = (By.XPATH,"//button[@data-test-id='goto-checkout-button']")
    complete_booking_btn = (By.XPATH,"//button[@id='complete-booking']")
    credit_card_error = (By.XPATH,"//label[@class='text cc-cardholder-name invalid']/p[@class='uitk-validation-error']")

    #User Details Below
    user_title = (By.XPATH,"//select[@id='title[0]']/option[@value='1_Mr.']")
    user_surname = (By.XPATH,"//input[@id='lastname[0]']")
    user_name = (By.XPATH,"//input[@id='firstname[0]']")
    user_email = (By.XPATH,"//input[@type='email' and @name='email' and @placeholder='Email for confirmation']")
    user_phone = (By.XPATH,"//input[@id='phone-number[0]']")
    user_dob_day = (By.XPATH,"//select[@id='date_of_birth_day[0]']/option[2]")
    user_dob_month = (By.XPATH,"//select[ @data-tealeaf-name='date_of_birth_month[0]']/option[2]")
    user_dob_year = (By.XPATH,"//select[@id='date_of_birth_year[0]']/option[30]")
    user_street = (By.XPATH,"//input[@name='street']")
    user_city = (By.XPATH,"//input[@name='city']")
    user_zipcode = (By.XPATH,"//input[@name='zipcode']")
    user_pan = (By.XPATH, "//input[@name='TAX.ID']")

class HotelBookingElements(CommonElements):

    dest_btn = (By.XPATH,"//button[@data-stid='destination_form_field-menu-trigger']")
    dest_input = (By.XPATH,"//section[@data-testid='popover-sheet']//input[@data-stid='destination_form_field-menu-input']")
    num_of_travellers = (By.XPATH,"//input[@id='traveler_selector_adult_step_input-0']")
    increase_travellers = (By.XPATH,"//*[@aria-label='Increase the number of adults in room 1']")
    decrease_travellers = (By.XPATH,"//*[@aria-label='Decrease the number of adults in room 1']")
    second_hotel = (By.XPATH,"//div[@data-stid='property-listing-results']/div[@class='uitk-spacing uitk-spacing-margin-blockstart-three'][2]")
    room_types = (By.XPATH,"//div[@data-stid='section-room-list']//div[starts-with(@class, '')]//h3[@class='uitk-heading uitk-heading-6']")