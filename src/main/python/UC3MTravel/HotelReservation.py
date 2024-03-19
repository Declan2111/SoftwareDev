
import hashlib
import json
from stdnum import es
from datetime import datetime
import re

class HotelReservation:
    def __init__(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type, numdays):
        self.__crEDITcardnumber = creditcardNumb
        self.__idcard = IDCARD
        justnow = datetime.utcnow()
        self.__ARRIVAL = datetime.timestamp(justnow)
        self.__NAME_SURNAME = nAMeAndSURNAME
        self.__phonenumber = phonenumber
        self.__roomtype = room_type
        self.__num_days = numdays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        if not self.checkCardNum(self.__crEDITcardnumber):
            raise ValueError("Invalid credit card number.")
        if not self.checkID(self.__idcard):
            raise ValueError("Invalid ID card.")
        if not self.checkName(self.__NAME_SURNAME):
            raise ValueError(
                "Name and surname must be between 10 and 50 characters and contain at least two strings separated by white space.")
        if not self.checkPhone(self.__phonenumber):
            raise ValueError("Invalid phone number.")
        if not self.checkRoom(self.__roomtype):
            raise ValueError("Invalid room type.")
        if not self.checkNumDays(self.__num_days):
            raise ValueError("Number of days must be a number between 1 and 10.")
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
    def LOCALIZER( self ):
        """Returns the md5 signature"""
        return hashlib.md5(self.__str__().encode()).hexdigest()

    def checkCardNum(self, card_number):
        card_str = str(card_number)
        if len(str(card_number)) != 16:
            return False

        total = 0
        for i in range(15):  # Loop through the first 15 digits
            digit = int(card_str[i])
            if i % 2 != 0:  # Only double the digit if its position is odd
                doubled_digit = digit * 2
                if doubled_digit > 9:
                    doubled_digit -= 9
                total += doubled_digit

        return total % 10 == int(card_str[15]) and len(str(card_number)) == 16

    def checkID(self, IDNum):
        return es.dni.is_valid(IDNum)

    def checkName(self, name):
        if isinstance(name, str):
            return 10 <= len(name) <= 50 and ' ' in name.strip()
        else:
            return False

    def checkPhone(self, PhoneNum):
        if isinstance(PhoneNum, int):
            return len(str(PhoneNum)) == 9 and int(PhoneNum) > 0
        else:
            return False

    def checkRoom(self, roomType):
        if isinstance(roomType, str):
            return roomType.lower() in ["single", "double", "suite"]
        else:
            return False

    def checkNumDays(self, numDays):
        if isinstance(numDays, int):
            return 0 < numDays < 11
        else:
            return False


