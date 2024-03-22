import hashlib
import json
import os

from stdnum import es
from datetime import datetime

from src.main.python.UC3MTravel import HotelManager
from src.main.python.UC3MTravel.HotelManagementException import HotelManagementException
# Move room_reservation and add_to_json to HotelManager, add excepetions to room_reservation function
#Keep the rest of the methods and the tests in HotelReservation

class HotelReservation:
    def __init__(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type, numdays):
        self.__crEDITcardnumber = creditcardNumb
        self.__idcard = IDCARD
        justnow = datetime.utcnow()
        self.__ARRIVAL = "30/05/2024" #datetime.timestamp(justnow)
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

    # def room_reservation(self, credit_card, name_surname, id_card, phone_number, room_type, arrival_date, num_days):
    #     if (self.checkCardNum(credit_card) and self.checkName(name_surname) and self.checkID(id_card)
    #             and self.checkPhone(phone_number) and self.checkRoom(room_type) and self.checkNumDays(num_days)):
    #         self.add_booking_to_json()
    #         return self.LOCALIZER
    #     else:
    #         raise HotelManagementException("Invalid Input Data")

#     def add_booking_to_json(self):
#         #localizer = self.LOCALIZER
#         booking_data = {
#                 "id_card": self.__idcard,
#                 "name_surname": self.__NAME_SURNAME,
#                 "credit_card": self.__crEDITcardnumber,
#                 "phone_number": self.__phonenumber,
#                 "arrival_date": self.__ARRIVAL,
#                 "num_days": self.__num_days,
#                 "room_type": self.__roomtype
#             }
#
#
#         if os.path.exists("bookings.json"):
#             with open("bookings.json", "r") as file:
#                 bookings = json.load(file)
#
#             # Check if id_card already exists in any entry
#             for entry in bookings:
#                 if 'id_card' in entry and entry['id_card'] == self.__idcard:
#                     print("Booking with the same id_card already exists.")
#                     return
#
#         else:
#             bookings = []
#
#         # Add the new booking data
#         bookings.append(booking_data)
#
#         # Write the updated bookings to the JSON file
#         with open("bookings.json", "w") as file:
#             json.dump(bookings, file, indent=4)
#
#         print("Booking successfully added.")
#
# # Example usage:
# reservation = HotelReservation("12345678Z", 4929319438123457, "Declan Lowney", 123456789, "single", 5)
# reservation.add_booking_to_json()

#manager = HotelManager()
#manager.add_booking_to_json(4929319438123457, "Declan Lowney", "12345678Z", 123456789, "suite", "21-03-2024", 5)