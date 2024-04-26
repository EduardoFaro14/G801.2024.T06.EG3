"""Module for the hotel manager"""
from .hotel_stay import HotelStay
from .storage.reservation_json_store import ReservationJsonStore
from .storage.stay_json_store import StayJsonStore
from .hotel_reservation import HotelReservation
from .parser.arrival_json_parser import ArrivalJsonParser
# pylint: disable=too-few-public-methods
class HotelManager:
    "Class hotel manager"
    # pylint: disable=invalid-name
    class __HotelManager:
        """Class with all the methods for managing reservations and stays"""
        def __init__(self):
            pass
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
            arrival_input = ArrivalJsonParser(file_input)
            my_id_card = arrival_input.json_content["IdCard"]
            my_localizer = arrival_input.json_content["Localizer"]
            my_checkin = HotelStay(my_id_card, my_localizer)
            checkin_store = StayJsonStore()
            checkin_store.add_item(my_checkin)

            return my_checkin.room_key

        def guest_checkout(self, room_key:str)->bool:
            """manages the checkout of a guest"""
            stay = HotelStay.get_stay_from_room_key(room_key)
            return stay

    __instance = None
    def __new__(cls):
        if not HotelManager.__instance:
            HotelManager.__instance = HotelManager.__HotelManager()
        return HotelManager.__instance
