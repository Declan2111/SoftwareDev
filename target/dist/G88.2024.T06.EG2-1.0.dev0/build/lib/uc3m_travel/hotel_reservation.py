"""File that contains the class that creates a hotel reservation for a guest"""
import hashlib
from datetime import datetime


class HotelReservation:
    """Class that creates a json file for guests hotel reservation bookings"""
    def __init__(self, idCard, creditcardNum, nameAndSurname, phoneNumber, roomType, arrival, numDays):
        self.creditCardNumber = creditcardNum
        self.idcard = idCard
        justnow = datetime.utcnow()
        self.arrival = arrival
        self.reservationDate = datetime.timestamp(justnow)
        self.nameSur = nameAndSurname
        self.phoneNum = phoneNumber
        self.room = roomType
        self.nDays = numDays

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        # VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        jsonInfo = {"id_card": self.idcard,
                     "name_surname": self.nameSur,
                     "credit_card": self.creditCardNumber,
                     "phone_number:": self.phoneNum,
                     "arrival_date": self.arrival,
                     "num_days": self.nDays,
                     "room_type": self.room,
                    }
        return "HotelReservation:" + jsonInfo.__str__()

    @property
    def creditCard(self):
        """gets the credit card number of a guest"""
        return self.creditCardNumber

    @property
    def phoneNumber(self):
        """gets the phone number of a booking"""
        return self.phoneNum

    @phoneNumber.setter
    def phoneNumber(self, value):
        self.phoneNum = value

    @property
    def arrivalDate(self):
        """gets the arrival date"""
        return self.arrival

    @arrivalDate.setter
    def arrivalDate(self, value):
        self.arrival = value

    @property
    def numDays(self):
        """gets the number of days for a stay"""
        return self.nDays

    @numDays.setter
    def numDays(self, value):
        self.nDays = value

    @property
    def roomType(self):
        """gets the room type"""
        return self.room

    @roomType.setter
    def roomType(self, value):
        self.room = value

    @property
    def nameSurname(self):
        """gets the name of a guest"""
        return self.nameSur

    @nameSurname.setter
    def nameSurname(self, value):
        self.nameSur = value

    @creditCard.setter
    def creditCard(self, value):
        self.creditCardNumber = value

    @property
    def idCard(self):
        """gets an ID card number"""
        return self.idcard

    @idCard.setter
    def idCard(self, value):
        self.idcard = value

    @property
    def localizer(self):
        """Returns the md5 signature"""
        return hashlib.md5(str(self).encode()).hexdigest()
