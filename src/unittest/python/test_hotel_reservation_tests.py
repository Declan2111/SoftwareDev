import datetime
import unittest
from gc import freeze

# from freezegun import freeze_time
from datetime import datetime

from freezegun import freeze_time

from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
from src.main.python.UC3MTravel.HotelManager import HotelManager
from src.main.python.UC3MTravel.HotelReservation import HotelReservation

ValidCardNum = 4929319438123457
ValidID = "12345678Z"
ValidName = "Ella Zaugg-James"
ValidPhone = 123456789
ValidRoom = "single"
ValidNumDays = 5
ValidArrivalDate = "30/05/2024"
JustNowDate = datetime.timestamp(datetime.utcnow())
ValidClass = HotelManager()
CCException = HotelManagementException("Invalid Credit Card Number")

#ValidReservation = HotelReservation(ValidCardNum, ValidID, ValidName, ValidPhone, ValidRoom, ValidNumDays)




class TestHotelReservation(unittest.TestCase):
    # tests a valid card number
    def testValidCard1(self):
        self.assertTrue(ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays))

    # def room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays):
    # tests an invalid card number - not luhns compliant
    def testInvalidCard1(self):
        #self.assertFalse(ValidClass.checkCardNum(4929319438123450))
        #Res1 = room_reservation(valid, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(4929319438123450, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    # tests an invalid card number - incorrect data type
    def testInvalidCard2(self):
        #self.assertFalse(ValidClass.checkCardNum("abcdefgh"))
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation("abcdefgh", ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    # tests an invalid card number - too many digits
    def testInvalidCard3(self):
        #self.assertFalse(ValidClass.checkCardNum(49293194381234578))
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(49293194381234578, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")


    # tests an invalid card number - too few digits
    def testInvalidCard4(self):
        #self.assertFalse(ValidClass.checkCardNum(492931943812345))
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(492931943812345, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    # tests a valid ID value
    def testValidID1(self):
        self.assertTrue(ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays))

    # tests an invalid ID value - letter does not correspond with number
    def testInvalidID1(self):
        #self.assertFalse(ValidClass.checkID("12345678A"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, "12345678A", ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    # tests an invalid ID value - too many characters
    def testInvalidID2(self):
        #self.assertFalse(ValidClass.checkID("123456789A"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, "123456789A", ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    # tests an invalid ID value - too few characters
    def testInvalidID3(self):
        #self.assertFalse(ValidClass.checkID("1234567A"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, "1234567A", ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid ID Number")



    # tests an invalid ID value - letter not at the end
    def testInvalidID4(self):
        #self.assertFalse(ValidClass.checkID("Z12345678"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, "Z12345678", ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    # tests an invalid ID data type
    def testInvalidID5(self):
        #self.assertFalse(ValidClass.checkID(12345678.9))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, 12345678.9, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid ID Number")



    # tests a valid name
    def testValidName1(self):
        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    # tests boundary value of 10 characters
    def testValidName2(self):
        #self.assertTrue(ValidClass.checkName("John Smith"))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, "John Smith", ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    # tests boundary value of 11 characters
    def testValidName3(self):
        #self.assertTrue(ValidClass.checkName("Jonny Smith"))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, "Jonny Smith", ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    # tests boundary value of 49 characters
    def testValidName4(self):
        #self.assertTrue(ValidClass.checkName("Alexandria Elizabeth Catherine Stephanie Jonathan"))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, "Alexandria Elizabeth Catherine Stephanie Jonathan", ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    # tests boundary value of 50 characters
    def testValidName5(self):
        #self.assertTrue(ValidClass.checkName("Alexandria Elizabeth Catherine Stephanie Jonathans"))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, "Alexandria Elizabeth Catherine Stephanie Jonathans", ValidID,
                                        ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))



    # tests boundary value of 51 characters
    def testInvalidName1(self):
        #self.assertFalse(ValidClass.checkName("Alexandria Elizabeth Catherines Stephanie Jonathans"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, "Alexandria Elizabeth Catherines Stephanie Jonathans", ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Name")

    # tests boundary value of 9 characters
    def testInvalidName2(self):
        #self.assertFalse(ValidClass.checkName("Jon Smith"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, "Jon Smith", ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Name")

    # tests incorrect data type
    def testInvalidName3(self):
        #self.assertFalse(ValidClass.checkName(1234))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, 1234, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Name")

    # tests name with no space in string
    def testInvalidName4(self):
        #self.assertFalse(ValidClass.checkName("DeclanLowney"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, "DeclanLowney", ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Name")

    # tests a valid phone number
    def testValidPhone1(self):
        #self.assertTrue(ValidClass.checkPhone(ValidPhone))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    # tests an invalid phone number boundary value
    def testInvalidPhone1(self):
        #self.assertFalse(ValidClass.checkPhone(12345678))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, 12345678, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Phone Number")

    # tests an invalid phone number boundary value
    def testInvalidPhone2(self):
        #self.assertFalse(ValidClass.checkPhone(1234567891))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, 1234567891, ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Phone Number")

    # tests an invalid phone number data type
    def testInvalidPhone3(self):
        #self.assertFalse(ValidClass.checkPhone("hellooooo"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, "hellooooo", ValidRoom, ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Phone Number")

    # tests room of type single
    def testValidRoom1(self):
        #self.assertTrue(ValidClass.checkRoom(ValidRoom))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    # tests room of type double
    def testValidRoom2(self):
        #self.assertTrue(ValidClass.checkRoom("double"))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "double", ValidArrivalDate,
                                        ValidNumDays))

    # tests room of type suite
    def testValidRoom3(self):
        #self.assertTrue(ValidClass.checkRoom("suite"))
        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "suite", ValidArrivalDate,
                                        ValidNumDays))


    # tests a string which is not a room
    def testInvalidRoom1(self):
        #self.assertFalse(ValidClass.checkRoom("hello"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "hello", ValidArrivalDate, ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Room Type")

    # tests an incorrect data type
    def testInvalidRoom2(self):
        #self.assertFalse(ValidClass.checkRoom(1234))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, 1234, ValidArrivalDate,
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Room Type")

    # tests a valid number of days to stay
    def testValidNumDays1(self):
        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "suite", ValidArrivalDate,
                                        ValidNumDays))

    # tests boundary value of valid number of days to stay
    def testValidNumDays2(self):
        #self.assertTrue(ValidClass.checkNumDays(1))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "suite", ValidArrivalDate,
                                        1))

    # tests boundary value of valid number of days to stay
    def testValidNumDays3(self):
        #self.assertTrue(ValidClass.checkNumDays(2))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "suite", ValidArrivalDate,
                                        2))

    # tests boundary value of valid number of days to stay
    def testValidNumDays4(self):
        #self.assertTrue(ValidClass.checkNumDays(10))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "suite", ValidArrivalDate,
                                        10))

    # tests boundary value of valid number of days to stay
    def testValidNumDay5(self):
        #self.assertTrue(ValidClass.checkNumDays(9))

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, "suite", ValidArrivalDate,
                                        9))

    # tests boundary value of invalid number of days to stay
    def testInvalidNumDays1(self):
        #self.assertFalse(ValidClass.checkNumDays(11))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        11)

        self.assertEqual(str(context.exception), "Invalid Number of Days")

    # tests boundary value of invalid number of days to stay
    def testInvalidNumDays2(self):
        #self.assertFalse(ValidClass.checkNumDays(0))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        0)

        self.assertEqual(str(context.exception), "Invalid Number of Days")

    # tests an incorrect data type for num days
    def testInvalidNumDays3(self):
        #self.assertFalse(ValidClass.checkNumDays("a"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        "a")

        self.assertEqual(str(context.exception), "Invalid Number of Days")

    def testValidArrival(self):

        self.assertTrue(
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate,
                                        ValidNumDays))

    def testInvalidArrival(self):
        #self.assertFalse(ValidClass.checkArrival("30-05-2024"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "30-05-2024",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival2(self):
        #self.assertFalse(ValidClass.checkArrival("32/05/2024"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "32/05/2024",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival3(self):
        #self.assertFalse(ValidClass.checkArrival("30/13/2024"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "30/13/2024",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival4(self):
        #self.assertFalse(ValidClass.checkArrival("30/05/20244"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "30/05/20244",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival5(self):
        #self.assertFalse(ValidClass.checkArrival("30/05/202"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "30/05/202",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival6(self):
        #self.assertFalse(ValidClass.checkArrival("3A/05/2024"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "3A/05/2024",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival7(self):
        #self.assertFalse(ValidClass.checkArrival("30/3Q/2024"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "30/3Q/2024",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def testInvalidArrival8(self):
        #self.assertFalse(ValidClass.checkArrival("30/05/20L4"))

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, "30/05/20L4",
                                        ValidNumDays)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    # @freeze_time("30/05/2024")
    # def testRoomReservation(self):
    #     self.assertEqual(ValidClass.room_reservation(ValidCardNum, ValidName, ValidID, ValidPhone, ValidRoom, ValidArrivalDate, ValidNumDays), ValidReservation.LOCALIZER)


