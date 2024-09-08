from utils.helper import CommonOps
from utils.elements import HotelBookingElements
import copy,time,json
class HotelPage(CommonOps,HotelBookingElements):
    def __init__(self,driver,url,no_of_people):
        super().__init__(driver)
        self.driver=driver
        self.url = url
        self.no_of_people = no_of_people
        
    def search_hotel(self,dest,guests):
        
        self.click(self.dest_btn)
        self.enter_text(self.dest_input,dest,sleep_time=5)

        self.click(self.date_tab)
        start_date = self.calculate_date(3)
        start_date = start_date.replace(" 0", " ")
        start_date_element = copy.deepcopy(self.date)
        start_date_element[-1] = start_date_element[-1].replace("ADD DATE HERE",start_date)
        start_date_element = tuple(start_date_element)
        self.click(start_date_element)

        end_date = self.calculate_date(4)
        end_date = start_date.replace(" 0", " ")
        end_date_element = copy.deepcopy(self.date)
        end_date_element[-1] = end_date_element[-1].replace("ADD DATE HERE",end_date)
        end_date_element = tuple(end_date_element)
        self.click(end_date_element)

        self.click(self.travellers_btn)
        if guests==1:
            self.click(self.decrease_travellers)

        self.click(self.done_btn)
        self.click(self.search_btn)
        


    def select_second_hotel(self):
        self.click(self.second_hotel)
        time.sleep(5)
        


    def extract_room_types(self):
        try:
            window_handles = self.driver.window_handles
            self.driver.switch_to.window(window_handles[-1])

            room_type = self.find_elements(self.room_types)
            rooms = []
            for room in room_type:
                room_name = room.text
                rooms.append({"room_type":room_name})

            with open('../room_details.json','w') as json_file:
                json.dump(rooms,json_file)
        except Exception as E:
            print(E)
            return False
        else:
            return "Room details stored !"
