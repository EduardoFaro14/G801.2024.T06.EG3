"""Module for the hotel manager"""
from uc3m_travel.hotel_stay import HotelStay
from .hotel_management_exception import HotelManagementException
from .storage.reservation_json_store import ReservationJsonStore
from .storage.stay_json_store import StayJsonStore
from .storage.checkout_json_store import CheckOutJsonStore
from .hotel_departure import HotelDeparture
from .attributes.attribute_room_key import RoomKey
from .hotel_reservation import HotelReservation
from .parser.arrival_json_parser import ArrivalJsonParser

class HotelManager:
    "Class hotel manager"
    class __HotelManager:
        """Class with all the methods for managing reservations and stays"""
        def __init__(self):
            pass
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
            arrival_input = ArrivalJsonParser(file_input)
            my_id_card = arrival_input.json_content["IdCard"]
            my_localizer = arrival_input.json_content["Localizer"]
            my_checkin = HotelStay(my_id_card, my_localizer)
            #my_checkin = HotelStay.create_guest_arrival_from_file(file_input)
            # añado el diccionario a la lista de checkins
            checkin_store = StayJsonStore()
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
