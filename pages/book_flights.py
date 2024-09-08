
from utils.helper import CommonOps
from utils.elements import FlightBookingElements
from datetime import datetime, timedelta
import time


class FlightPage(CommonOps,FlightBookingElements):
    def __init__(self,driver,url,no_of_people):
        super().__init__(driver)
        self.driver=driver
        self.url = url
        self.no_of_people = no_of_people
        
    def search_flight(self,source,dest,traveller):
        
        # Calculate the date 3 days from now
        formatted_date = self.calculate_date(3)
        formatted_date = formatted_date.replace(" 0", " ")
        
        # Move to flight tab
        self.click(self.flight_tab)
        
        # Select one way
        self.click(self.one_way)

        # Add source and destination
        self.click(self.source_btn)
        self.enter_text(self.source_input,source,sleep_time=5)
        self.click(self.dest_btn)
        self.enter_text(self.dest_input,dest,sleep_time=5)

        # Select Date
        self.click(self.date_tab)
        self.date[-1] = self.date[-1].replace("ADD DATE HERE",formatted_date)
        self.date = tuple(self.date)
        self.click(self.date)

        # Select done and click search button
        self.click(self.done_btn)

        if traveller==2:
            self.click(self.travellers_btn)
            self.click(self.increase_traveller)

        self.click(self.search_btn)

    def sort_results(self):
        self.click(self.shortest_duration)
        self.click(self.flight_list)
        

    def select_cheapest_flight(self):
        self.click(self.flight_list)
        self.click(self.select_shortest_cheapest_flight)

    def proceed_to_checkout(self):
        self.click(self.details_and_fare_page)
        self.click(self.select_button)

        time.sleep(5)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

        self.click(self.checkout_button)
        time.sleep(5)

    def enter_user_details(self,
                           user_name,
                           user_surname,
                           user_email,
                           user_mobile,
                           user_street,
                           user_city,
                           user_zipcode,
                           user_pan
                           ):
        self.click(self.user_title)
        self.enter_text(self.user_surname,user_surname)
        self.enter_text(self.user_name,user_name)
        self.enter_text(self.user_email,user_email)
        self.enter_text(self.user_phone,user_mobile)
        self.click(self.user_dob_day)
        self.click(self.user_dob_month)
        self.click(self.user_dob_year)
        self.enter_text(self.user_street,user_street)
        self.enter_text(self.user_city,user_city)
        self.enter_text(self.user_zipcode,user_zipcode)
        self.enter_text(self.user_pan,user_pan)

    def complete_booking_return_error(self) -> str:
        self.click(self.complete_booking_btn)
        time.sleep(5)
        error_text = self.click(self.credit_card_error,return_text=True)

        return error_text

