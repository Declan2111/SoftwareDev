""" Class HotelStay (GE2.2) """

from datetime import datetime, timedelta
import hashlib


class HotelStay:
    """Creates an instance of a guest staying in a hotel"""

    def __init__(self, idcard, localizer, numdays, roomtype):
        self.alg1 = "SHA-256"
        self.type = roomtype
        self.idcard = idcard
        self.loc = localizer
        justnow = datetime.utcnow()
        self.arrivalDate = justnow
        # timestamp is represented in seconds.milliseconds
        # to add the number of days we must express numdays in seconds
        numSeconds = numdays * 24 * 60 * 60

        # Create a timedelta object for num_seconds
        delta = timedelta(seconds=numSeconds)

        # Add the timedelta to self.__arrival to get the departure time
        self.departDate = self.arrivalDate + delta

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.alg1 + ",typ:" + self.type + ",localizer:" + \
            self.loc + ",arrival:" + str(self.arrivalDate) + \
            ",departure:" + str(self.departDate) + "}"

    @classmethod
    def from_departure(cls, idcard, localizer, departure, roomType, arrival):
        """Alternate constructor for HotelStay using information in the stay json file"""
        obj = cls(idcard, localizer, 3, roomType)
        obj.arrivalDate = arrival
        obj.departDate = departure
        return obj

    @property
    def idCard(self):
        """Property that represents the product_id of the patient"""
        return self.idcard

    @idCard.setter
    def idCard(self, value):
        self.idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.loc

    @localizer.setter
    def localizer(self, value):
        self.loc = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.arrivalDate

    @property
    def roomKey(self):
        """Returns the sha256 signature of the date"""
        return hashlib.sha256(self.__signature_string().encode()).hexdigest()

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.departDate

    @departure.setter
    def departure(self, value):
        self.departDate = value

    def alg(self):
        """returns SHA-256"""
        return self.alg1

    def typ(self):
        """returns the room type of the stay"""
        return self.type
