#THIS MAIN PROGRAM IS ONLY VALID FOR THE FIRST THREE WEEKS OF CLASS
#IN GUIDED EXERCISE 2.2, TESTING MUST BE PERFORMED USING UNITTESTS.

from src.main.python.UC3MTravel import hotel_manager


def main():
    mng = HotelManager()
    res = mng.read_data_from_json("test.json")
    strRes = res.__str__()
    print(strRes)
    print("CreditCard: " + res.creditCard)
    print(res.localizer)

if __name__ == "__main__":
    main()
