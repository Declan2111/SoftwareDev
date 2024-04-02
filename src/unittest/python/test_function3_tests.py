"""File containing the class testing function 3"""
import json
import os
import unittest
from freezegun import freeze_time

from uc3m_travel import HotelManagementException
from uc3m_travel.hotel_manager import HotelManager

v_res1 = HotelManager()
v_localizer1 = v_res1.room_reservation(4929319438123457, 'Nathan Damstra',
                                       '99999999R', 123456789, 'double',
                                       '27/05/2024', 3)

guest_file = {"Localizer": v_localizer1, "IdCard": "99999999R"}
with open("guest_file_TC.json", "w", encoding= "utf-8") as file:
    json.dump(guest_file, file, indent=4)

with freeze_time("27/05/2024"):
    v_room_key1 = v_res1.guest_arrival("guest_file_TC.json")



class TestFunction3(unittest.TestCase):
    """Class containing the class testing function 3"""
    def test_case1(self):
        """1-11: no stays.json file"""
        os.remove("stays.json")
        with freeze_time("30/05/2024"):
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout(v_room_key1)
            self.assertEqual(str(context.exception), "stays file does not exist")

    def test_case2(self):
        """1-2-3-10: no entries in stays.json file"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        with freeze_time("30/05/2024"):
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout(v_room_key1)
            self.assertEqual(str(context.exception), "no room key exists in stay file.")

    def test_case3(self):
        """no matching room key in the entries"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
        "alg": "SHA-256",
        "typ": "double",
        "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
        "idCard": "99999999R",
        "arrival": "2024-05-27T00:00:00",
        "departure": "2024-05-30T00:00:00",
        "room_key": "74ebc2e2876a9eb2815fef93282342558492552a4f8998eaeb60d71d85017098"
    }], file, indent=4)
        with freeze_time("30/05/2024"):
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout(v_room_key1)
            self.assertEqual(str(context.exception), "no room key exists in stay file.")

    def test_case4(self):
        """ valid through everything"""
        os.remove("checkouts.json")
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
        "alg": "SHA-256",
        "typ": "double",
        "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
        "idCard": "99999999R",
        "arrival": "2024-05-27T00:00:00",
        "departure": "2024-05-30T00:00:00",
        "room_key": v_room_key1
            }], file, indent=4)
        with freeze_time("30/05/2024"):
            self.assertTrue(v_res1.guest_checkout(v_room_key1))

    def test_case5(self):
        """room key not a string"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
                "alg": "SHA-256",
                "typ": "double",
                "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
                "idCard": "99999999R",
                "arrival": "2024-05-27T00:00:00",
                "departure": "2024-05-30T00:00:00",
                "room_key": 123456
            }], file, indent=4)
        with freeze_time("30/05/2024"):
            room_key = 123456
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout(room_key)
            self.assertEqual(str(context.exception), "room key not valid format")

    def test_case6(self):
        """1 - 2 - 3 - 4 - 5 - 6 - 12 - 13 - 28: room key invalid length"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
                "alg": "SHA-256",
                "typ": "double",
                "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
                "idCard": "99999999R",
                "arrival": "2024-05-27T00:00:00",
                "departure": "2024-05-30T00:00:00",
                "room_key": "74ebc2e2876a9eb2815fef93282342558492552a998eaeb60d71d85017098"
            }], file, indent=4)
        with freeze_time("30/05/2024"):
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout("74ebc2e2876a9eb2815fef93282342558492552a998eaeb60d71d85017098")
            self.assertEqual(str(context.exception), "room key not valid format")

    def test_case7(self):
        """room key not alphanumerical"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
                "alg": "SHA-256",
                "typ": "double",
                "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
                "idCard": "99999999R",
                "arrival": "2024-05-27T00:00:00",
                "departure": "2024-05-30T00:00:00",
                "room_key": "74ebc2e2876a9eb2815fef9328234/558492552a4f8998eaeb60d71d85017098"
            }], file, indent=4)
        with freeze_time("30/05/2024"):
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout("74ebc2e2876a9eb2815fef9328234/558492552a4f8998eaeb60d71d85017098")
            self.assertEqual(str(context.exception), "room key not valid format")

    def test_case8(self):
        """room key is not all lower case"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
                "alg": "SHA-256",
                "typ": "double",
                "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
                "idCard": "99999999R",
                "arrival": "2024-05-27T00:00:00",
                "departure": "2024-05-30T00:00:00",
                "room_key": "74EBc2e2876a9eb2815fef9328234/558492552a4f8998eaeb60d71d85017098"
            }], file, indent=4)
        with freeze_time("30/05/2024"):
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout("74EBc2e2876a9eb2815fef9328234/558492552a4f8998eaeb60d71d85017098")
            self.assertEqual(str(context.exception), "room key not valid format")

    def test_case9(self):
        """room key does not match the data"""


    def test_case10(self):
        """valid case if checkouts does not exist yet"""
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump([{
                "alg": "SHA-256",
                "typ": "double",
                "localizer": "5b07fc19e6151c0a624c44bbcb3cf7fc",
                "idCard": "99999999R",
                "arrival": "2024-05-27T00:00:00",
                "departure": "2024-05-30T00:00:00",
                "room_key": v_room_key1
            }], file, indent=4)
        if os.path.exists('checkouts.json'):
            os.remove('checkouts.json')
        with freeze_time("30/05/2024"):
            self.assertTrue(v_res1.guest_checkout(v_room_key1))

    def test_case11(self):
        """exception if room_key already exists in checkouts json"""
        with freeze_time("30/05/2024"):
            with open("checkouts.json", "w", encoding="utf-8") as file:
                json.dump([{
                    "timestamp": 1717027200.0,
                    "room_key": v_room_key1
                }], file, indent=4)
            with self.assertRaises(HotelManagementException) as context:
                v_res1.guest_checkout(v_room_key1)
            self.assertEqual(str(context.exception), "checkout with the same room key already exists.")












