import unittest

from src.main.python.UC3MTravel import HotelManager
from src.main.python.UC3MTravel.HotelReservation import HotelReservation

ValidCardNum = 4929319438123457
ValidID = "12345678Z"
ValidName = "Ella Zaugg-James"
ValidPhone = 123456789
ValidRoom = "single"
ValidNumDays = 5
ValidClass = HotelManager()


class TestHotelReservation(unittest.TestCase):
    # tests a valid card number
    def testValidCard1(self):
        self.assertTrue(ValidClass.checkCardNum(ValidCardNum))

    # tests an invalid card number - not luhns compliant
    def testInvalidCard1(self):
        self.assertFalse(ValidClass.checkCardNum(4929319438123450))

    # tests an invalid card number - incorrect data type
    def testInvalidCard2(self):
        self.assertFalse(ValidClass.checkCardNum("abcdefgh"))

    # tests an invalid card number - too many digits
    def testInvalidCard3(self):
        self.assertFalse(ValidClass.checkCardNum(49293194381234578))

    # tests an invalid card number - too few digits
    def testInvalidCard4(self):
        self.assertFalse(ValidClass.checkCardNum(492931943812345))

    # tests a valid ID value
    def testValidID1(self):
        self.assertTrue(ValidClass.checkID(ValidID))

    # tests an invalid ID value - letter does not correspond with number
    def testInvalidID1(self):
        self.assertFalse(ValidClass.checkID("12345678A"))

    # tests an invalid ID value - too many characters
    def testInvalidID2(self):
        self.assertFalse(ValidClass.checkID("123456789A"))

    # tests an invalid ID value - too few characters
    def testInvalidID3(self):
        self.assertFalse(ValidClass.checkID("1234567A"))

    # tests an invalid ID value - letter not at the end
    def testInvalidID4(self):
        self.assertFalse(ValidClass.checkID("Z12345678"))

    # tests an invalid ID data type
    def testInvalidID5(self):
        self.assertFalse(ValidClass.checkID(12345678.9))

    # tests a valid name
    def testValidName1(self):
        self.assertTrue(ValidClass.checkName(ValidName))

    # tests boundary value of 10 characters
    def testValidName2(self):
        self.assertTrue(ValidClass.checkName("John Smith"))

    # tests boundary value of 11 characters
    def testValidName3(self):
        self.assertTrue(ValidClass.checkName("Jonny Smith"))

    # tests boundary value of 49 characters
    def testValidName4(self):
        self.assertTrue(ValidClass.checkName("Alexandria Elizabeth Catherine Stephanie Jonathan"))

    # tests boundary value of 50 characters
    def testValidName5(self):
        self.assertTrue(ValidClass.checkName("Alexandria Elizabeth Catherine Stephanie Jonathans"))

    # tests boundary value of 51 characters
    def testInvalidName1(self):
        self.assertFalse(ValidClass.checkName("Alexandria Elizabeth Catherines Stephanie Jonathans"))

    # tests boundary value of 9 characters
    def testInvalidName2(self):
        self.assertFalse(ValidClass.checkName("Jon Smith"))

    # tests incorrect data type
    def testInvalidName3(self):
        self.assertFalse(ValidClass.checkName(1234))

    # tests name with no space in string
    def testInvalidName4(self):
        self.assertFalse(ValidClass.checkName("DeclanLowney"))

    # tests a valid phone number
    def testValidPhone1(self):
        self.assertTrue(ValidClass.checkPhone(ValidPhone))

    # tests an invalid phone number boundary value
    def testInvalidPhone1(self):
        self.assertFalse(ValidClass.checkPhone(12345678))

    # tests an invalid phone number boundary value
    def testInvalidPhone2(self):
        self.assertFalse(ValidClass.checkPhone(1234567891))

    # tests an invalid phone number data type
    def testInvalidPhone3(self):
        self.assertFalse(ValidClass.checkPhone("hellooooo"))

    # tests room of type single
    def testValidRoom1(self):
        self.assertTrue(ValidClass.checkRoom(ValidRoom))

    # tests room of type double
    def testValidRoom2(self):
        self.assertTrue(ValidClass.checkRoom("double"))

    # tests room of type suite
    def testValidRoom3(self):
        self.assertTrue(ValidClass.checkRoom("suite"))

    # tests a string which is not a room
    def testInvalidRoom1(self):
        self.assertFalse(ValidClass.checkRoom("hello"))

    # tests an incorrect data type
    def testInvalidRoom2(self):
        self.assertFalse(ValidClass.checkRoom(1234))

    # tests a valid number of days to stay
    def testValidNumDays1(self):
        self.assertTrue(ValidClass.checkNumDays(ValidNumDays))

    # tests boundary value of valid number of days to stay
    def testValidNumDays2(self):
        self.assertTrue(ValidClass.checkNumDays(1))

    # tests boundary value of valid number of days to stay
    def testValidNumDays3(self):
        self.assertTrue(ValidClass.checkNumDays(2))

    # tests boundary value of valid number of days to stay
    def testValidNumDays4(self):
        self.assertTrue(ValidClass.checkNumDays(10))

    # tests boundary value of valid number of days to stay
    def testValidNumDay5(self):
        self.assertTrue(ValidClass.checkNumDays(9))

    # tests boundary value of invalid number of days to stay
    def testInvalidNumDays1(self):
        self.assertFalse(ValidClass.checkNumDays(11))

    # tests boundary value of invalid number of days to stay
    def testInvalidNumDays2(self):
        self.assertFalse(ValidClass.checkNumDays(0))

    # tests an incorrect data type for num days
    def testInvalidNumDays3(self):
        self.assertFalse(ValidClass.checkNumDays("a"))
