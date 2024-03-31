''' Class HotelStay (GE2.2) '''

from datetime import datetime, date, time, timedelta
import hashlib

class HotelStay():
    def __init__(self, idcard, localizer, numdays, roomtype):
        self.__alg = "SHA-256"
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = justnow
        #timestamp is represented in seconds.miliseconds
        #to add the number of days we must express numdays in seconds
        num_seconds = numdays * 24 * 60 * 60

        # Create a timedelta object for num_seconds
        delta = timedelta(seconds=num_seconds)

        # Add the timedelta to self.__arrival to get the departure time
        self.__departure = self.__arrival + delta

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__alg + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @classmethod
    def from_departure(cls, idcard, localizer, departure, roomtype, arrival):
        obj = cls(idcard, localizer, 0, roomtype)
        obj.__arrival = arrival
        obj.__departure = departure
        return obj

    @property
    def idCard(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @idCard.setter
    def idCard(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value

    def alg(self):
        return self.__alg

    def typ(self):
        return self.__type







