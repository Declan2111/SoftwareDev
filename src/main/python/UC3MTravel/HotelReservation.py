import hashlib
import json
import os

# from stdnum import es
from datetime import datetime

# from UC3MTravel.HotelManager import HotelManager
from UC3MTravel.HotelManagementException import HotelManagementException
# Move room_reservation and add_to_json to HotelManager, add excepetions to room_reservation function
#Keep the rest of the methods and the tests in HotelReservation

class HotelReservation:
    def __init__(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type, arrival, numdays):
        self.__crEDITcardnumber = creditcardNumb
        self.__idcard = IDCARD
        justnow = datetime.utcnow()
        self.__ARRIVAL = arrival
        self.__reservationdate = datetime.timestamp(justnow)
        self.__NAME_SURNAME = nAMeAndSURNAME
        self.__phonenumber = phonenumber
        self.__roomtype = room_type
        self.__num_days = numdays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        # VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__idcard,
                     "name_surname": self.__NAME_SURNAME,
                     "credit_card": self.__crEDITcardnumber,
                     "phone_number:": self.__phonenumber,
                     "arrival_date": self.__ARRIVAL,
                     "num_days": self.__num_days,
                     "room_type": self.__roomtype,
                     }
        return "HotelReservation:" + json_info.__str__()

    @property
    def CREDITCARD(self):
        return self.__crEDITcardnumber

    @property
    def phone_number(self):
        return self.__phonenumber

    @property
    def arrival_date(self):
        return self.__ARRIVAL

    @property
    def num_days(self):
        return self.__num_days

    @property
    def room_type(self):
        return self.__roomtype

    @property
    def name_surname(self):
        return self.__NAME_SURNAME

    @CREDITCARD.setter
    def CREDITCARD(self, value):
        self.__crEDITcardnumber = value

    @property
    def IDCARD(self):
        return self.__idcard

    @IDCARD.setter
    def IDCARD(self, value):
        self.__idcard = value

    @property
    def LOCALIZER(self):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()


#
# # Example usage:
# reservation = HotelReservation("12345678Z", 4929319438123457, "Declan Lowney", 123456789, "single", 5)
# reservation.add_booking_to_json()

#manager = HotelManager()
#manager.add_booking_to_json(4929319438123457, "Declan Lowney", "12345678Z", 123456789, "suite", "21-03-2024", 5)