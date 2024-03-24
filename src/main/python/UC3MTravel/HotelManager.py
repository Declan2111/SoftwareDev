import json
import os
from datetime import datetime
import re

from stdnum import es

from UC3MTravel.HotelManagementException import HotelManagementException
from UC3MTravel.HotelReservation import HotelReservation
from UC3MTravel.HotelStay import HotelStay


class HotelManager:
    def __init__(self):
        #these are the dictionaries I was referring to in the manipulation checkers
        self.reservations = {}
        self.stays = {}
        self.identifier = {}

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


    def checkArrival(self, arrival_date):
        pattern = r"\b(0[1-9]|[12]\d|3[01])[/](0[1-9]|1[0-2])[/](19\d\d|20\d\d)\b"
        date_regex = re.compile(pattern)
        return date_regex.search(arrival_date)

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
        if not self.checkCardNum(c):
            raise HotelManagementException("Invalid credit card number")

        # Close the file
        return req


    def room_reservation(self, credit_card, name_surname, id_card, phone_number, room_type, arrival_date, num_days):
        #function 1
        if (self.checkCardNum(credit_card) and self.checkName(name_surname) and self.checkID(id_card)
                and self.checkPhone(phone_number) and self.checkRoom(room_type) and self.checkNumDays(num_days) and self.checkArrival(arrival_date)):
            reservation = HotelReservation(id_card, credit_card, name_surname, phone_number, room_type, arrival_date, num_days)
            localizer = reservation.LOCALIZER
            ### check localizer with a new method and if statement!?
            self.add_booking_to_json(credit_card, name_surname, id_card, phone_number, room_type, arrival_date, num_days, localizer)
            self.reservations[localizer] = reservation
            self.identifier[id_card] = localizer
            return localizer
        else:
            raise HotelManagementException("Invalid Input Data")

    def add_booking_to_json(self, credit_card, name_surname, id_card, phone_number, room_type, arrival_date, num_days, localizer):
        #function 1
        # reservation = HotelReservation(id_card, credit_card, name_surname, phone_number, room_type, num_days)
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





    def guest_arrival(self, guest_file):
        #function 2
        #idk if we have to create our own method to create the input, or if we have to worrry about it
        #in case we do, I've created 2 seperate methods to accomplish creating this file: guest_provides_info1&2
        self.validate_guest_file(guest_file)
        with open(guest_file, "r") as file:
            guest_data = json.load(file)

            localizer = guest_data["Localizer"]
            id = guest_data["IDCard"]
            with open("bookings.json", "r") as bookings:
                bookings = json.load(bookings)
                for entry in bookings:
                    if 'localizer' in entry and entry['localizer'] == localizer:
                        if 'id_card' in entry and entry['id_card'] == id:
                            num_days = entry["num_days"]
                            room_type = entry["room_type"]
                            # self.check_manipulation() #this where we would check that the localizer matches the data in the bookings json
                            if (self.checkCardNum(entry['credit_card']) and self.checkName(entry['name_surname']) and self.checkID(
                                    id) and self.checkPhone(entry['phone_number']) and self.checkRoom(
                                        room_type) and self.checkNumDays(num_days) and self.checkArrival(entry['arrival_date'])):
                                stay = HotelStay(id, localizer, num_days, room_type)
                                self.add_stay_to_json(stay, localizer)
                                return stay.room_key()
                        else:
                            return print("id card doesn't match")
                print("no localizer found in reservation file")

    def validate_guest_file(self, guest_file):
        #function 2
        #syntatical analysis
        return True

    def guest_provides_info1(self, id_card, credit_card):
        #function 2?
        #dependent on weather we can store a dict of id cards to quickly receive the location
        #problem: if same id makes multiple different reservations
        #generates input for function 2 guest_arrival method, then calls guest_arrival
        # guest_file = self.generate_guest_file(id_card)
        if self.identifier.__contains__(id_card):
            file_name = "guest_" + str(id_card) + "_file" + ".json"
            with open(file_name, "w") as file:
                guest_data = {"Localizer": self.identifier[id_card], "IDCard": id_card}
                json.dump(guest_data, file, indent=4)
            self.guest_arrival(file_name)

    def guest_provides_info2(self, id_card, credit_card):
        #function 2?
        #essentially retrieves the localizer in the bookings json from the the provided id_card
        #calls function2 guest_arrival
        if os.path.exists("bookings.json"):
            with open("bookings.json", "r") as file:
                bookings = json.load(file)
            for entry in bookings:
                if 'id_card' in entry and entry['id_card'] == id_card:
                    print("id card matches a reservation!")
                    if 'localizer' in entry:
                        localizer = entry['localizer']

                        guest_info = {"Localizer": localizer, "IDCard": id_card}
                        guest_info_entry = []
                        guest_info_entry.append(guest_info)
                        file_name = "guest_" + str(id_card) + "file" + ".json"
                        with open(file_name, "w") as new_file:
                            json.dump(guest_info_entry, new_file, indent=4)
                        self.guest_arrival(file_name)
                    else:
                        return print("No localizer in bookings")
            else:
                return print("No matching id card in bookings")
        else:
            print("No bookings file exists")


    def check_manipulation1(self, name_surname, credit_card, num_days, room_type, phone_number, arrival_date, id_card, localizer):
        #function 2
        #this method is dependent on if we can store the reservation objects in a dictionary. check __init__
        # if so we update the date in that object and generate a localizer.
        #since the object has already been instantiated, the datetime should be the same and thus if the data updated is the same then the localizer should be the same.
        if self.reservations.__contains__(localizer):
            reservation = self.reservations[localizer]
        else:
            return print("no localizer found in reservations dict")
        if (self.checkCardNum(credit_card) and self.checkName(name_surname) and self.checkID(
                id_card) and self.checkPhone(phone_number) and self.checkRoom(
            room_type) and self.checkNumDays(num_days) and self.checkArrival(arrival_date)):
            reservation.CREDITCARD(credit_card)
            reservation.IDCARD(id_card)
            reservation.room_type(room_type)
            reservation.phone_number(phone_number)
            reservation.arrival_date(arrival_date)
            reservation.num_days(num_days)
            reservation.name_surname(name_surname)
            new_locator = reservation.LOCALIZER()
            if localizer == new_locator:
                print("no manipulation to data in reservation file (locator matches the information)")
                return True
            else:
                print("appears to have manipulation in the file")
                return False

    def check_manipulation2(self, id_card, credit_card, name_surname, phone_number, room_type, arrival_date, localizer_freezed):
        #function 2
        #if we use this method then we would have to include localizer_freeze to bookings file. this method utilizes a new method in Reservation: LOCALIZER_FREEZED
        #im thinking this is the best option since it doesn't depend on storing a reservation object dictionary.
        reservation_test = HotelReservation(id_card, credit_card, name_surname, phone_number, room_type, arrival_date)
        new_loc_freezed = reservation_test.LOCALIZER_FREEZED()
        if new_loc_freezed == localizer_freezed:
            print("no manipulation to data in reservation")
            return True
        else:
            print("manipulation is present in reservation file")
            return False

    def check_manipulation3(self, localizer):
        #function 2
        #this method is dependent on if we can store the reservation objects in a dictionary; check __init__
        #it compares weather the data in the reservation object matches the data in the JSON file.
        if self.reservations.__contains__(localizer):
            reservation = self.reservations[localizer]
        else:
            return print("no localizer found in reservations dict")
        with open("bookings.json", "r") as bookings:
            bookings = json.load(bookings)
            for entry in bookings:
                if 'localizer' in entry and entry['localizer'] == localizer:
                    if entry['num_days'] == reservation.num_days():
                        if entry['room_type'] == reservation.room_type():
                            if entry['credit_card'] == reservation.CREDITCARD():
                                if entry['phone_number'] == reservation.phone_number():
                                    if entry['id_card'] == reservation.IDCARD():
                                        if entry['name_surname'] == reservation.name_surname():
                                            if entry['arrival_date'] == reservation.arrival_date():
                                                return True
                                            else:
                                                return print("wrong arrival")
                                        else:
                                            return print("wrong name")
                                    else:
                                        return print("wrong id_card")
                                else:
                                    return print("wrong phone")
                            else:
                                return print("wrong credit")
                        else:
                            return print("wrong room_type")
                    else:
                        return print("wrong num_days")
            else:
                return print("localizer not in bookings")









    def check_manipulation4(self, IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type, arrival, numdays, localizer):
        #function 2
        #same logic as #4 but without the freeze time so this won't work, but a good start if theres another idea on how to check manipulation
        reservation = HotelReservation(IDCARD, creditcardNumb, nAMeAndSURNAME, phonenumber, room_type, arrival, numdays)
        current_loc = reservation.LOCALIZER
        if current_loc == localizer:
            print("no manipulation")
            return True
        else:
            print("manipulation or the localizer doesn't match")
            return False

    def add_stay_to_json(self, stay, localizer):
        #function 2
        cur_stay = {
            "alg": stay.alg(),
            "typ": stay.typ(),
            "localizer": localizer,
            "arrival": stay.arrival(),
            "departure": stay.departure(),
            "room_key": stay.room_key()
        }

        if os.path.exists("stays.json"):
            with open("stays.json", "r") as file:
                stay_data = json.load(file)

            # Check if id_card already exists in any entry
            for entry in stay_data:
                if 'localizer' in entry and entry['localizer'] == localizer:
                    print("Stay with the same localizer already exists.")
                    return

        else:
            stay_data = []

        # Add the new booking data
        stay_data.append(cur_stay)

        # Write the updated bookings to the JSON file
        with open("stays.json", "w") as file:
            json.dump(stay_data, file, indent=4)

        print("Stay successfully added.")


    def guest_checkout(self, room_key):
        #function 3!

        self.validate_room_key(room_key)
        if os.path.exists("stays.json"):
            with open("stays.json", "r") as file:
                stay_data = json.load(file)
                for entry in stay_data:
                    if "room_key" in entry and entry["room_key"] == room_key:
                        alg = entry["alg"]
                        typ = entry["typ"]
                        localizer = entry["localizer"]
                        arrival = entry["arrival"]
                        departure = entry["departure"]
                        self.departure_date_valid(departure)
                        self.add_checkout_to_json(room_key)
                        print("checkout was successfully validated")
                        return True
                print("no room key exists in stay file.")
                return False
        else:
            print("stays file does not exist")
            return False




    def validate_room_key(self, room_key):
        #function 3
        #syntatical analysis
        #returns true if room_key is in the correct format
        return True

    def departure_date_valid(self, departure_date):
        #function 3
        #returns true if the request to checkout is on the same day as there scheduled "departure date"
        #use datetime to compare
        return True

    def add_checkout_to_json(self, room_key):
        #function 3
        #adds timestamp and room_key to checkouts json file
        justnow = datetime.utcnow()
        timestamp = datetime.timestamp(justnow)
        checkout = {
            "timestamp": timestamp,
            "room_key": room_key
        }
        if os.path.exists("checkouts.json"):
            with open("checkouts.json", "r") as file:
                checkout_data = json.load(file)

            # Check if id_card already exists in any entry
            for entry in checkout_data:
                if 'room_key' in entry and entry['room_key'] == room_key:
                    print("checkout with the same room key already exists.")
                    return
        else:
            checkout_data = []
        # Add the new booking data
        checkout_data.append(checkout)
        # Write the updated bookings to the JSON file
        with open("checkouts.json", "w") as file:
            json.dump(checkout_data, file, indent=4)
        print("checkout successfully added.")











# reservation = HotelReservation("12345678Z", 4929319438123457, "Declan Lowney", 123456789, "single", 5)
# reservation.add_booking_to_json()

#manager = HotelManager()
#manager.add_booking_to_json(4929319438123457, "Declan Lowney", "12345678Z", 123456789, "suite", "21-03-2024", 5)