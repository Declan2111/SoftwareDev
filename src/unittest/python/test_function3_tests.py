
import unittest
from freezegun import freeze_time

from uc3m_travel import HotelManagementException
from uc3m_travel import HotelManager

v_res1 = HotelManager()
v_localizer1 = v_res1.room_reservation('123456789', 'Nathan Damstra', '4929319438123457', '123456789', 'double', '05/30/2024', '3')

guest_file = {"Localizer": v_localizer1, "IDCard": "123456789"}
with open("guest_file_TC.json" "w", encoding= "utf-8") as file:
    json.dump(guest_file, file, indent=4)

class TestFunction3(unittest.TestCase):
    def



