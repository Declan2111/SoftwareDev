import json
import os

from .HotelManagementException import HotelManagementException
from .HotelReservation import HotelReservation
from stdnum import es

class HotelManager:
    def __init__(self):
        pass

    # Checks that the credit card number is valid following Luhn's Algorithm
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

    # Checks that the ID is valid based on Spanish ID standards
    def checkID(self, IDNum):
        return es.dni.is_valid(IDNum)

    # Checks that the name is a valid name with a space in between two strings
    def checkName(self, name):
        if isinstance(name, str):
            return 10 <= len(name) <= 50 and ' ' in name.strip()
        else:
            return False

    # Checks that the phone is a valid number
    def checkPhone(self, PhoneNum):
        if isinstance(PhoneNum, int):
            return len(str(PhoneNum)) == 9 and int(PhoneNum) > 0
        else:
            return False

    # Checks that the room type is correct
    def checkRoom(self, roomType):
        if isinstance(roomType, str):
            return roomType.lower() in ["single", "double", "suite"]
        else:
            return False

    # Checks that the number of days is in between 1 and 10
    def checkNumDays(self, numDays):
        if isinstance(numDays, int):
            return 0 < numDays < 11
        else:
            return False

    def ReaddatafromJSOn( self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            c = DATA["CreditCard"]
            p = DATA["phoneNumber"]
            req = HotelReservation(IDCARD="12345678Z",creditcardNumb=c,nAMeAndSURNAME="John Doe",phonenumber=p,room_type="single",numdays=3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.validatecreditcard(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req


    def room_reservation(self, credit_card, name_surname, id_card, phone_number, room_type, arrival_date, num_days):
        if (self.checkCardNum(credit_card) and self.checkName(name_surname) and self.checkID(id_card)
                and self.checkPhone(phone_number) and self.checkRoom(room_type) and self.checkNumDays(num_days)):
            reservation = HotelReservation(id_card, credit_card, name_surname, phone_number, room_type, num_days)
            reservation.add_booking_to_json()
            return reservation.LOCALIZER
        else:
            raise HotelManagementException("Invalid Input Data")

    def add_booking_to_json(self, credit_card, name_surname, id_card, phone_number, room_type, arrival_date, num_days):
        reservation = HotelReservation(id_card, credit_card, name_surname, phone_number, room_type, num_days)
        localizer = reservation.LOCALIZER
        booking_data = {
                "id_card": id_card,
                "name_surname": name_surname,
                "credit_card": credit_card,
                "phone_number": phone_number,
                "arrival_date": arrival_date,
                "num_days": num_days,
                "room_type": room_type,
                "localizer": localizer
            }

        if os.path.exists("bookings.json"):
            with open("bookings.json", "r") as file:
                bookings = json.load(file)

            # Check if id_card already exists in any entry
            for entry in bookings:
                if 'id_card' in entry and entry['id_card'] == id_card:
                    print("Booking with the same id_card already exists.")
                    return

        else:
            bookings = []

        # Add the new booking data
        bookings.append(booking_data)

        # Write the updated bookings to the JSON file
        with open("bookings.json", "w") as file:
            json.dump(bookings, file, indent=4)

        print("Booking successfully added.")