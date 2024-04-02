"""File containing the HotelManager class"""

import json
import os
from datetime import datetime
import datetime as dt
import re
from stdnum import es
from .hotel_management_exception import HotelManagementException
from .hotel_reservation import HotelReservation
from .hotel_stay import HotelStay


class HotelManager:
    """Class containing the functionality for managing hotel reservations and handling guest activity"""
    def __init__(self):
        self.reservations = {}
        self.stays = {}
        self.identifier = {}

    def check_card_num(self, cardNumber):
        """Checks that the credit card number is valid following Luhn's Algorithm"""
        cardStr = str(cardNumber)
        if len(str(cardNumber)) != 16:
            raise HotelManagementException("Invalid Credit Card Number")

        total = 0
        for i in range(15):  # Loop through the first 15 digits
            digit = int(cardStr[i])
            if i % 2 != 0:  # Only double the digit if its position is odd
                doubledDigit = digit * 2
                if doubledDigit > 9:
                    doubledDigit -= 9
                total += doubledDigit

        if total % 10 == int(cardStr[15]) and len(str(cardNumber)) == 16:
            return True
        raise HotelManagementException("Invalid Credit Card Number")

    def check_id(self, idNum):
        """Checks that the ID is valid based on Spanish ID standards"""
        if es.dni.is_valid(idNum):
            return True
        raise HotelManagementException("Invalid ID Number")

    def check_name(self, name):
        """Checks that the name is a valid name with a space in between two strings"""
        if isinstance(name, str) and (10 <= len(name) <= 50 and ' ' in name.strip()):
            return True
        raise HotelManagementException("Invalid Name")

    def check_phone(self, phoneNum):
        """Checks that the phone is a valid number"""
        if isinstance(phoneNum, int) and (len(str(phoneNum)) == 9 and int(phoneNum) > 0):
            return True
        raise HotelManagementException("Invalid Phone Number")

    def check_room(self, roomType):
        """Checks that the room type is correct"""
        if isinstance(roomType, str) and (roomType.lower() in ["single", "double", "suite"]):
            return True
        raise HotelManagementException("Invalid Room Type")

    def check_num_days(self, numDays):
        """Checks that the number of days is in between 1 and 10"""
        if isinstance(numDays, int) and (0 < numDays < 11):
            return True
        raise HotelManagementException("Invalid Number of Days")

    def check_arrival(self, arrivalDate):
        """Checks that the arrival date is in the correct format"""
        pattern = r"\b(0[1-9]|[12]\d|3[01])[/](0[1-9]|1[0-2])[/](19\d\d|20\d\d)\b"
        dateRegex = re.compile(pattern)
        if dateRegex.search(arrivalDate):
            return True
        raise HotelManagementException("Invalid Arrival Date")

    def read_data_from_json(self, fi):
        """Reads given data and make sure JSON format is valid"""
        try:
            with open(fi, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            c = data["CreditCard"]
            p = data["phoneNumber"]
            req = HotelReservation("12345678Z", c, "John Doe", p, "single", "19/06/2026", 3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.check_card_num(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req

    def room_reservation(self, creditCard, nameSurname, idCard, phoneNumber, roomType, arrivalDate, numDays):
        """Checks all input data is valid and creates a localizer for the data"""
        # function 1
        if (self.check_card_num(creditCard) and self.check_name(nameSurname) and self.check_id(idCard)
                and self.check_phone(phoneNumber) and self.check_room(roomType) and self.check_num_days(
                    numDays) and self.check_arrival(arrivalDate)):
            reservation = HotelReservation(idCard, creditCard, nameSurname, phoneNumber,
                                           roomType, arrivalDate, numDays)
            localizer = reservation.localizer
            self.add_booking_to_json(creditCard, nameSurname, idCard, phoneNumber, roomType,
                                     arrivalDate, numDays, localizer)
            self.reservations[localizer] = reservation
            self.identifier[idCard] = localizer
            return localizer
        raise HotelManagementException("Invalid Input Data")

    def add_booking_to_json(self, creditCard, nameSurname, idCard, phoneNumber, roomType,
                            arrivalDate, numDays, localizer):
        """Adds all the given data for a reservation to the bookings JSON file"""
        # function 1
        bookingData = {
            "id_card": idCard,
            "name_surname": nameSurname,
            "credit_card": creditCard,
            "phone_number": phoneNumber,
            "arrival_date": arrivalDate,
            "num_days": numDays,
            "room_type": roomType,
            "localizer": localizer
        }

        if os.path.exists("bookings.json"):
            with open("bookings.json", "r", encoding="utf-8") as file:
                bookings = json.load(file)

            # Check if id_card already exists in any entry
            for entry in bookings:
                if 'id_card' in entry and entry['id_card'] == idCard:
                    print("Booking with the same id_card already exists.")
                    return

        else:
            bookings = []

        # Add the new booking data
        bookings.append(bookingData)

        # Write the updated bookings to the JSON file
        with open("bookings.json", "w", encoding="utf-8") as file:
            json.dump(bookings, file, indent=4)

        print("Booking successfully added.")

    def guest_arrival(self, guestFile):
        """Validates that the guest data has a booking in
        the bookings file with the same data as when booked"""
        # function 2
        self.validate_guest_file(guestFile)
        with open(guestFile, "r", encoding="utf-8") as file:
            guestData = json.load(file)

            localizer = guestData["Localizer"]
            iD = guestData["IdCard"]

            # make sure there aren't more than one localizer or IDCard keys
            localizerCount = 0
            idCardCount = 0

            for item in guestData:
                if 'Localizer' in item:
                    localizerCount += 1

            for item in guestData:
                if 'IdCard' in item:
                    idCardCount += 1

            if localizerCount > 1 or idCardCount > 1:
                raise HotelManagementException("Key Error: More than one Localizer or IdCard found")
            with open("bookings.json", "r", encoding="utf-8") as bookings:
                bookings = json.load(bookings)
                for entry in bookings:
                    if 'localizer' in entry and entry['localizer'] == localizer:
                        if 'id_card' in entry and entry['id_card'] == iD:
                            creditCard = entry["credit_card"]
                            name = entry["name_surname"]
                            arrival = entry["arrival_date"]
                            idCard = entry["id_card"]
                            numDays = entry["num_days"]
                            roomType = entry["room_type"]
                            phoneNumber = entry["phone_number"]
                            localizerNum = entry["localizer"]
                            self.check_manipulation(idCard, creditCard, name, phoneNumber, roomType, arrival,
                                                    numDays, localizerNum)
                            if (self.check_card_num(entry['credit_card']) and self.check_name(
                                    entry['name_surname']) and self.check_id(
                                iD) and self.check_phone(entry['phone_number']) and self.check_room(
                                roomType) and self.check_num_days(numDays) and self.check_arrival(
                                entry['arrival_date'])):
                                stay = HotelStay(iD, localizer, numDays, roomType)
                                self.add_stay_to_json(stay, localizer)
                                return stay.roomKey
                raise HotelManagementException("Error: Localizer or ID not found in bookings file")

    def validate_guest_file(self, guestFile):
        """Check to make sure input file follows valid json format and meets assignment requirements"""
        try:
            with open(guestFile, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError as e:
            raise HotelManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            _ = data["Localizer"]
            p = data["IdCard"]
            validCardNum = 4929319438123457
            validName = "Ella Zaugg-James"
            validPhone = 123456789

            req = HotelReservation(p, validCardNum, validName, validPhone, "single", "30/05/2024", 3)
        except KeyError as e:
            raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from e

        # Close the file
        return req

    def check_manipulation(self, idCard, creditCard, nameSurname, phoneNumber, roomType, arrivalDate,
                           numDays, localizer):
        """Checks to make sure the data corresponding to a localizer has not been manipulated"""
        reservationTest = HotelReservation(idCard, creditCard, nameSurname, phoneNumber,
                                           roomType, arrivalDate, numDays)
        newLoc = reservationTest.localizer
        if newLoc == localizer:
            print("no manipulation to data in reservation")
            return True
        raise HotelManagementException("Manipulation is present in reservation file")

    def guest_checkout(self, roomKey):
        """Records the guest leaving the room, validating the key and departure date are correct,
        the adding the checkout to a file"""
        if os.path.exists("stays.json"):
            with open("stays.json", "r", encoding="utf-8") as file:
                stayData = json.load(file)
                for entry in stayData:
                    if "room_key" in entry and entry["room_key"] == roomKey:
                        # alg = entry["alg"]
                        roomtype = entry["typ"]
                        localizer = entry["localizer"]
                        arrival = entry["arrival"]
                        departure = entry["departure"]
                        idcard = entry["idCard"]
                        # checks format and if it matches stay data
                        self.validate_room_key(roomKey, idcard, roomtype, localizer, arrival, departure)
                        self.departure_date_valid(departure)
                        self.add_checkout_to_json(roomKey)
                        print("checkout was successfully validated")
                        return True
                print("no room key exists in stay file.")
                raise HotelManagementException("no room key exists in stay file.")
        else:
            print("stays file does not exist")
            raise HotelManagementException("stays file does not exist")

    def validate_room_key(self, roomKey, iD, roomtype, localizer, arrival, departure):
        """Checks the room key is a valid format and in the stay file"""
        # function 3
        # check format
        if not isinstance(roomKey, str) or len(roomKey) != 64 \
                or not roomKey.isalnum() or not roomKey.islower():
            raise HotelManagementException("room key not valid format")
        # Now we know key is valid format, so we check if it is in the stay json file
        # stay = HotelStay.from_departure(iD, localizer, departure, roomtype, arrival)
        # if stay.roomKey == roomKey:
        #     return True
        # raise HotelManagementException("room key doesn't match stay information")

    def departure_date_valid(self, departureDate):
        """Checks that the departure date the guest is leaving is the same as the current date"""
        # function 3
        currentDate = dt.date.today()
        dt_object = datetime.strptime(departureDate, '%Y-%m-%dT%H:%M:%S')

        # Format the datetime object into the desired format
        givenDate = dt_object.strftime('%d/%m/%Y')
        return givenDate == currentDate

    def add_checkout_to_json(self, roomKey):
        """adds timestamp and room_key to checkouts json file"""
        # function 3
        justnow = datetime.utcnow()
        timestamp = datetime.timestamp(justnow)
        checkout = {
            "timestamp": timestamp,
            "room_key": roomKey
        }
        if os.path.exists("checkouts.json"):
            with open("checkouts.json", "r", encoding="utf-8") as file:
                checkoutData = json.load(file)

            # Check if id_card already exists in any entry
            for entry in checkoutData:
                if 'room_key' in entry and entry['room_key'] == roomKey:
                    print("checkout with the same room key already exists.")
                    raise HotelManagementException("checkout with the same room key already exists.")
        else:
            checkoutData = []
        # Add the new booking data
        checkoutData.append(checkout)
        # Write the updated bookings to the JSON file
        with open("checkouts.json", "w", encoding="utf-8") as file:
            json.dump(checkoutData, file, indent=4)
        print("checkout successfully added.")

    def add_stay_to_json(self, stay, localizer):
        """adds guest stay information to the stay json file"""
        # function 2
        curStay = {
            "alg": stay.alg(),
            "typ": stay.typ(),
            "localizer": localizer,
            "idCard": stay.idCard,
            "arrival": stay.arrival.isoformat(),
            "departure": stay.departure.isoformat(),
            "room_key": stay.roomKey
        }

        if os.path.exists("stays.json"):
            with open("stays.json", "r", encoding="utf-8") as file:
                stayData = json.load(file)

            # Check if id_card already exists in any entry
            for entry in stayData:
                if 'localizer' in entry and entry['localizer'] == localizer:
                    print("Stay with the same localizer already exists.")
                    return

        else:
            stayData = []

        # Add the new booking data
        stayData.append(curStay)

        # Write the updated bookings to the JSON file
        with open("stays.json", "w", encoding="utf-8") as file:
            json.dump(stayData, file, indent=4)

        print("Stay successfully added.")
