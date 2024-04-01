"""File containing the class testing function 2"""
import unittest
from freezegun import freeze_time

from src.main.python.UC3MTravel.hotel_management_exception import HotelManagementException
from src.main.python.UC3MTravel.hotel_manager import HotelManager

ValidClass = HotelManager()


class TestFunction2(unittest.TestCase):
    """Class for testing the functionality of function 2 using syntax analysis"""

    @freeze_time("30/05/2024")
    def test_case1(self):
        """Test valid file"""
        self.assertEqual(ValidClass.guest_arrival("JSONTests/TC1.json"),
                         "fe6d6300551b5f6c861ac23ea051c2914f853709a144c42cfe4b0e3b28d9c09b")

    def test_case2(self):
        """Test delete node 1"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC2.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case3(self):
        """Test duplicate node 1"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC3.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case4(self):
        """Test delete node 2"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC4.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case5(self):
        """Test duplicate node 2"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC5.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case6(self):
        """Modifiy node 5"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC6.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case7(self):
        """Delete node 3"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC7.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case8(self):
        """Duplicate node 3"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC8.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case9(self):
        """Delete node 4"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC9.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case10(self):
        """Duplicate node 4"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC10.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case11(self):
        """Modify node 9"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC11.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case12(self):
        """Delete node 6"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC12.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case13(self):
        """Duplicate node 6"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC13.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case14(self):
        """Delete Node 7"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC14.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case15(self):
        """Duplicate node 7"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC15.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case16(self):
        """Node 17 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC16.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case17(self):
        """Node 8 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC17.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case18(self):
        """Node 8 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC18.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case19(self):
        """Node 10 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC19.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case20(self):
        """Node 10 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC20.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case21(self):
        """Node 25 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC21.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")  # Node 25 modified

    def test_case22(self):
        """Node 11 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC22.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case23(self):
        """Node 11 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC23.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case24(self):
        """Node 26 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC24.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case25(self):
        """Node 12 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC25.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case26(self):
        """Node 12 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC26.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case27(self):
        """Node 27 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC27.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case28(self):
        """Node 13 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC28.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case29(self):
        """Node 13 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC29.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case30(self):
        """Node 28 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC30.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case31(self):
        """Node 14 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC31.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case32(self):
        """Node 14 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC32.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case33(self):
        """Node 29 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC33.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case34(self):
        """Node 15 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC34.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    def test_case35(self):
        """Node 15 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC35.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case36(self):
        """Node 30 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC36.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    def test_case37(self):
        """Node 16 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC37.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case38(self):
        """Node 16 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC38.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case39(self):
        """Node 31 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC39.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case40(self):
        """Node 18 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC40.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case41(self):
        """Node 18 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC41.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case42(self):
        """Node 32 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC42.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case43(self):
        """Node 19 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC43.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case44(self):
        """Node 19 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC44.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case45(self):
        """Node 33 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC45.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    def test_case46(self):
        """Node 20 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC46.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case47(self):
        "Node 20 duplicated"
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC47.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case48(self):
        """Node 34 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC48.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case49(self):
        """Node 21 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC49.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case50(self):
        """Node 21 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC50.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case51(self):
        """Node 35 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC51.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case52(self):
        """Node 22 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC52.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case53(self):
        """Node 22 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC53.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case54(self):
        """Node 36 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC54.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case55(self):
        """Node 23 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC55.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    def test_case56(self):
        """Node 23 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC56.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    def test_case57(self):
        """Node 37 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC57.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    def test_case58(self):
        """Node 24 deleted"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC58.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case59(self):
        """Node 24 duplicated"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC59.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    def test_case60(self):
        """Node 38 modified"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC60.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    @freeze_time("30/05/2024")
    def test_manip1(self):
        """Testing Manipulation"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/ManipulationTest1.json")
        self.assertEqual(str(context.exception), "Manipulation is present in reservation file")

    @freeze_time("30/03/2024")
    def test_date_check(self):
        """checks date comparison works"""
        self.assertTrue(ValidClass.departure_date_valid("30/03/2024"))
