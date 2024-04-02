"""File that contains the class for tests for the room reservation function"""
import unittest
from datetime import datetime
from freezegun import freeze_time
from uc3m_travel import HotelManagementException
from uc3m_travel import HotelManager
from uc3m_travel import HotelReservation

VALID_CARD_NUM = 4929319438123457
VALID_ID = "12345678Z"
VALID_NAME = "Ella Zaugg-James"
VALID_PHONE = 123456789
VALID_ROOM = "single"
VALID_NUM_DAYS = 5
VALID_ARRIVAL_DATE = "30/05/2024"
JustNowDate = datetime.timestamp(datetime.utcnow())
ValidClass = HotelManager()
CCException = HotelManagementException("Invalid Credit Card Number")

ValidReservation = HotelReservation(VALID_CARD_NUM, VALID_ID, VALID_NAME, VALID_PHONE,
                                    VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS)


class TestHotelReservation(unittest.TestCase):
    """Testing the hotel reservation function using equivalence classes
    and boundary values to check the inputs"""

    def test_valid_card1(self):
        """tests a valid card number"""
        self.assertTrue(ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                                    VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_invalid_card1(self):
        """tests an invalid card number - not luhns compliant"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(4929319438123450, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    def test_invalid_card2(self):
        """tests an invalid card number - incorrect data type"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation("abcdefgh", VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    def test_invalid_card3(self):
        """tests an invalid card number - too many digits"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(49293194381234578, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    def test_invalid_card4(self):
        """tests an invalid card number - too few digits"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(492931943812345, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Credit Card Number")

    def test_valid_id1(self):
        """tests a valid ID value"""
        self.assertTrue(ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                                    VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_invalid_id1(self):
        """tests an invalid ID value - letter does not correspond with number"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, "12345678A", VALID_PHONE,
                                        VALID_ROOM, VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    def test_invalid_id2(self):
        """tests an invalid ID value - too many characters"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, "123456789A", VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    def test_invalid_id3(self):
        """tests an invalid ID value - too few characters"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, "1234567A", VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    def test_invalid_id4(self):
        """tests an invalid ID value - letter not at the end"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, "Z12345678", VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    def test_invalid_id5(self):
        """tests an invalid ID data type"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, 12345678.9, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid ID Number")

    def test_valid_name1(self):
        """tests a valid name"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_valid_name2(self):
        """tests boundary value of 10 characters"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, "John Smith", VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE,
                                        VALID_NUM_DAYS))

    def test_valid_name3(self):
        """tests boundary value of 11 characters"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, "Jonny Smith", VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE,
                                        VALID_NUM_DAYS))

    def test_valid_name4(self):
        """tests boundary value of 49 characters"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, "Alexandria Elizabeth Catherine Stephanie Jonathan",
                                        VALID_ID, VALID_PHONE, VALID_ROOM, VALID_ARRIVAL_DATE,
                                        VALID_NUM_DAYS))

    def test_valid_name5(self):
        """tests boundary value of 50 characters"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, "Alexandria Elizabeth Catherine Stephanie Jonathans",
                                        VALID_ID, VALID_PHONE, VALID_ROOM, VALID_ARRIVAL_DATE,
                                        VALID_NUM_DAYS))

    def test_invalid_name1(self):
        """tests boundary value of 51 characters"""

        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, "Alexandria Elizabeth Catherines Stephanie Jonathans",
                                        VALID_ID,VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Name")

    def test_invalid_name2(self):
        """tests boundary value of 9 characters"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, "Jon Smith", VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Name")

    def test_invalid_name3(self):
        """tests incorrect data type"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, 1234, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Name")

    def test_invalid_name4(self):
        """tests name with no space in string"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, "DeclanLowney", VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Name")

    def test_valid_phone1(self):
        """tests a valid phone number"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_invalid_phone1(self):
        """tests an invalid phone number boundary value"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, 12345678, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Phone Number")

    def test_invalid_phone2(self):
        """tests an invalid phone number boundary value"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, 1234567891, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Phone Number")

    def test_invalid_phone3(self):
        """tests an invalid phone number data type"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, "hellooooo", VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Phone Number")

    def test_valid_room1(self):
        """tests room of type single"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_valid_room2(self):
        """tests room of type double"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "double",
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_valid_room3(self):
        """tests room of type suite"""
        # self.assertTrue(ValidClass.checkRoom("suite"))
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "suite",
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_invalid_room1(self):
        """tests a string which is not a room"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "hello",
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Room Type")

    def test_invalid_room2(self):
        """tests an incorrect data type"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, 1234,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Room Type")

    def test_valid_num_days1(self):
        """tests a valid number of days to stay"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "suite",
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_valid_num_days2(self):
        """tests boundary value of valid number of days to stay"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "suite",
                                        VALID_ARRIVAL_DATE, 1))

    def test_valid_num_days3(self):
        """tests boundary value of valid number of days to stay"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "suite",
                                        VALID_ARRIVAL_DATE, 2))

    def test_valid_num_days4(self):
        """tests boundary value of valid number of days to stay"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "suite",
                                        VALID_ARRIVAL_DATE, 10))

    def test_valid_num_days5(self):
        """tests boundary value of valid number of days to stay"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, "suite",
                                        VALID_ARRIVAL_DATE, 9))

    def test_invalid_num_days1(self):
        """tests boundary value of invalid number of days to stay"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, 11)

        self.assertEqual(str(context.exception), "Invalid Number of Days")

    def test_invalid_num_days2(self):
        """tests boundary value of invalid number of days to stay"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, 0)

        self.assertEqual(str(context.exception), "Invalid Number of Days")

    def test_invalid_num_days3(self):
        """tests an incorrect data type for num days"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE,
                                        "a")

        self.assertEqual(str(context.exception), "Invalid Number of Days")

    def test_valid_arrival(self):
        """Tests a valid arrival date"""
        self.assertTrue(
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        VALID_ARRIVAL_DATE, VALID_NUM_DAYS))

    def test_invalid_arrival1(self):
        """Tests arrival date in the incorrect format"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE, VALID_ROOM,
                                        "30-05-2024", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival2(self):
        """Tests invalid arrival date - day doesnt exist"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "32/05/2024", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival3(self):
        """Tests invalid arrival date - month doesnt exist"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "30/13/2024", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival4(self):
        """Tests invalid arrival date - year too many chars"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "30/05/20244", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival5(self):
        """Tests invalid arrival date - year too few chars"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "30/05/202", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival6(self):
        """Tests invalid arrival date - letter in day"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "3A/05/2024", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival7(self):
        """Tests invalid arrival date - letter in month"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "30/3Q/2024", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    def test_invalid_arrival8(self):
        """Tests invalid arrival date - letter in year"""
        with self.assertRaises(HotelManagementException) as context:
            ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID, VALID_PHONE,
                                        VALID_ROOM, "30/05/20L4", VALID_NUM_DAYS)

        self.assertEqual(str(context.exception), "Invalid Arrival Date")

    @freeze_time("30/05/2024")
    def test_room_reservation(self):
        """Tests that the correct localizer is created given certain data"""
        self.assertEqual(ValidClass.room_reservation(VALID_CARD_NUM, VALID_NAME, VALID_ID,
                                                     VALID_PHONE, VALID_ROOM,
                                                     VALID_ARRIVAL_DATE, VALID_NUM_DAYS),
                         "c45cdbc85ababf7d4c215d77a767c94d")

    def testThing(self):
        self.assertTrue(ValidClass.room_reservation(4929319438123457, "Delcan Lowney", "01234567L",
                                                        123456789, "double", "29/07/2024", 6))
