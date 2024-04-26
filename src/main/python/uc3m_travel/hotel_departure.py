"Module hotel_departure"
from datetime import datetime
from .hotel_management_exception import HotelManagementException

class HotelDeparture:
    """Class to manage the departure of guests from the hotel"""
    def __init__(self, room_key, departure):
        self.room_key = room_key
        self.checkout_time = datetime.timestamp(datetime.utcnow())
        self.check_departure(departure)

    def check_departure(self, departure):
        "Function check departure"
        datenow = datetime.utcnow().date()
        if datetime.fromtimestamp(departure).date() != datenow:
            raise HotelManagementException("Error: today is not the departure day")
