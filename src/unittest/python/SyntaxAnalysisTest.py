import unittest

from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager

ValidClass = HotelManager()

class TestFunction2(unittest.TestCase):
#Test valid file
    #def testCase1(self):
        #self.assertEqual(ValidClass.guest_arrival("JSONTests/TC1.json"), "ae1ca44a9aca5c20283add2000306b7e59c39ca37f36d1dac79fdc9682d17955")

#Test delete node 1
    def testCase2(self):

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.guest_arrival("JSONTests/TC2.json")

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    #def testCase3(self):