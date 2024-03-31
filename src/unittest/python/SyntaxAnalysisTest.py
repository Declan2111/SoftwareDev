import unittest
from freezegun import freeze_time
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager

ValidClass = HotelManager()


class TestFunction2(unittest.TestCase):

    # Test valid file
    @freeze_time("30/05/2024")
    def testCase1(self):
        self.assertEqual(ValidClass.guest_arrival("JSONTests/TC1.json"),
                         "fe6d6300551b5f6c861ac23ea051c2914f853709a144c42cfe4b0e3b28d9c09b")

    # Test delete node 1
    def testCase2(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC2.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Test duplicate node 1
    def testCase3(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC3.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Test delete node 2
    def testCase4(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC4.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Test duplicate node 2
    def testCase5(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC5.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Modifiy node 5
    def testCase6(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC6.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Delete node 3
    def testCase7(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC7.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Duplicate node 3
    def testCase8(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC8.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Delete node 4
    def testCase9(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC9.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Duplicate node 4
    def testCase10(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC10.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Modify node 9
    def testCase11(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC11.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Delete node 6
    def testCase12(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC12.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Duplicate node 6
    def testCase13(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC13.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Delete Node 7
    def testCase14(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC14.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Duplicate node 7
    def testCase15(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC15.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 17 modified
    def testCase16(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC16.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 8 deleted
    def testCase17(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC17.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 8 duplicated
    def testCase18(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC18.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 10 deleted
    def testCase19(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC19.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 10 duplicated
    def testCase20(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC20.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 25 modified
    def testCase21(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC21.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")  # Node 25 modified

    # Node 11 deleted
    def testCase22(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC22.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Node 11 duplicated
    def testCase23(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC23.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Node 26 modified
    def testCase24(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC24.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Node 12 deleted
    def testCase25(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC25.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 12 duplicated
    def testCase26(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC26.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 27 modified
    def testCase27(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC27.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 13 deleted
    def testCase28(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC28.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 13 duplicated
    def testCase29(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC29.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 28 modified
    def testCase30(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC30.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 14 deleted
    def testCase31(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC31.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 14 duplicated
    def testCase32(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC32.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 29 modified
    def testCase33(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC33.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 15 deleted
    def testCase34(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC34.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    # Node 15 duplicated
    def testCase35(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC35.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 30 modified
    def testCase36(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC36.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    # Node 16 deleted
    def testCase37(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC37.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 16 duplicated
    def testCase38(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC38.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 31 modified
    def testCase39(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC39.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 18 deleted
    def testCase40(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC40.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 18 duplicated
    def testCase41(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC41.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 32 modified
    def testCase42(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC42.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 19 deleted
    def testCase43(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC43.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Node 19 duplicated
    def testCase44(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC44.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Node 33 modified
    def testCase45(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC45.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Invalid JSON Key")

    # Node 20 deleted
    def testCase46(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC46.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 20 duplicated
    def testCase47(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC47.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 34 modified
    def testCase48(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC48.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 21 deleted
    def testCase49(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC49.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 21 duplicated
    def testCase50(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC50.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 35 modified
    def testCase51(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC51.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 22 deleted
    def testCase52(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC52.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 22 duplicated
    def testCase53(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC53.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 36 modified
    def testCase54(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC54.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 23 deleted
    def testCase55(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC55.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    # Node 23 duplicated
    def testCase56(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC56.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    # Node 37 modified
    def testCase57(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC57.json")

        self.assertEqual(str(context.exception), "Error: Localizer or ID not found in bookings file")

    # Node 24 deleted
    def testCase58(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC58.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 24 duplicated
    def testCase59(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC59.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Node 38 modified
    def testCase60(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC60.json")

        self.assertEqual(str(context.exception), "JSON Decode Error - Wrong JSON Format")

    # Testing Manipulation
    @freeze_time("30/05/2024")
    def testManip1(self):
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/ManipulationTest1.json"),
        self.assertEqual(str(context.exception), "Manipulation is present in reservation file")