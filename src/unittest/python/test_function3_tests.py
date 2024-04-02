import json
import unittest
from freezegun import freeze_time

from src.main.python.uc3m_travel import HotelManagementException
#from src.main import python
from src.main.python.uc3m_travel.hotel_manager import HotelManager

v_res1 = HotelManager()
v_localizer1 = v_res1.room_reservation(4929319438123457, 'Nathan Damstra', '99999999R', 123456789, 'double', '27/05/2024', 3)

guest_file = {"Localizer": v_localizer1, "IdCard": "99999999R"}
with open("guest_file_TC.json", "w", encoding= "utf-8") as file:
    json.dump(guest_file, file, indent=4)





class TestFunction3(unittest.TestCase):
    def test_case1(self):
        with freeze_time("27/05/2024"):
            v_room_key1 = v_res1.guest_arrival("guest_file_TC.json")
        with freeze_time("30/05/2024"):
            self.assertTrue(v_res1.guest_checkout(v_room_key1))






