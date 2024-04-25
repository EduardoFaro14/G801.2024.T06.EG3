"""Module for the hotel manager"""
import re
import json
from datetime import datetime
from .hotel_management_exception import HotelManagementException
from .hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from .hotel_management_config import JSON_FILES_PATH
from freezegun import freeze_time
from .attributes.attribute_localizer import Localizer
from .attributes.attribute_idcard import IdCard
from .storage.json_store import JsonStore
from .storage.reservation_json_store import ReservationJsonStore
from .storage.stay_json_store import StayJsonStore
from .storage.checkout_json_store import CheckOutJsonStore
from .hotel_departure import HotelDeparture
from .attributes.attribute_roomkey import RoomKey
from .hotel_reservation import HotelReservation

class HotelManager:
    class __HotelManager:
        """Class with all the methods for managing reservations and stays"""
        def __init__(self):
            pass
        def read_data_from_json(self, fi):
            """reads the content of a json file with two fields: CreditCard and phoneNumber"""
            try:
                with open(fi, encoding='utf-8') as file:
                    json_data = json.load(file)
            except FileNotFoundError as exception:
                raise HotelManagementException("Wrong file or file path") from exception
            except json.JSONDecodeError as exception:
                raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception
            try:
                credit_card = json_data["CreditCard"]
                phone_number = json_data["phoneNumber"]
                data = HotelReservation(id_card="12345678Z",
                                       credit_card_number=credit_card,
                                       name_surname="John Doe",
                                       phone_number=phone_number,
                                       room_type="single",
                                       num_days=3,
                                       arrival="20/01/2024")
            except KeyError as exception:
                raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from exception
            #if not self.validatecreditcard(c):
                #raise HotelManagementException("Invalid credit card number")
            # Close the file
            return data

        # pylint: disable=too-many-arguments
        def room_reservation(self,
                             credit_card:str,
                             name_surname:str,
                             id_card:str,
                             phone_number:str,
                             room_type:str,
                             arrival_date: str,
                             num_days:int)->str:
            """manges the hotel reservation: creates a reservation and saves it into a json file"""
            my_reservation = HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)
            reservation_store = ReservationJsonStore()
            reservation_store.add_item(my_reservation)

            return my_reservation.localizer

        def guest_arrival(self, file_input: str) -> str:
            """manages the arrival of a guest with a reservation"""
            checkin_store = StayJsonStore()
            input_list = checkin_store.load_list_from_file(file_input)

            # comprobar valores del fichero
            try:
                my_localizer = Localizer(input_list["Localizer"]).value
                my_id_card = IdCard(input_list["IdCard"]).value
            except KeyError as e:
                raise HotelManagementException("Error - Invalid Key in JSON") from e

            # genero la room key para ello llamo a Hotel Stay
            my_checkin = HotelStay(idcard=my_id_card, localizer=my_localizer)

            # añado el diccionario a la lista de checkins
            checkin_store.add_item(my_checkin)

            return my_checkin.room_key

        def guest_checkout(self, room_key:str)->bool:
            """manages the checkout of a guest"""
            #check thawt the roomkey is stored in the checkins file
            room_key = RoomKey(room_key).value
            room_key_list = StayJsonStore()
            room_key_list = room_key_list.read_store()
            # comprobar que esa room_key es la que me han dado

            found = False
            for item in room_key_list:
                if room_key == item["_HotelStay__room_key"]:
                    departure_date_timestamp = item["_HotelStay__departure"]
                    found = True
            if not found:
                raise HotelManagementException ("Error: room key not found")

            my_checkout = HotelDeparture(room_key, departure_date_timestamp)
            checkout_store = CheckOutJsonStore()
            checkout_store.add_item(my_checkout)
            return True

    __instance = None
    def __new__(cls):
        if not HotelManager.__instance:
            HotelManager.__instance = HotelManager.__HotelManager()
        return HotelManager.__instance
