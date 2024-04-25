import json

from ..hotel_management_config import JSON_FILES_PATH
from .json_store import JsonStore
from uc3m_travel.hotel_management_exception import HotelManagementException

class ReservationJsonStore(JsonStore):
    class __ReservationJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_reservation.json"
        _data_list = []
        _error_message_find = ""

        def add_item(self, item):
            self._error_message_find = "Reservation already exists"
            self.find_item("_HotelReservation__localizer", item.localizer)
            self._error_message_find = "This ID card has another reservation"
            self.find_item("_HotelReservation__id_card", item.id_card)
            super().add_item(item)

    __instance = None
    def __new__(cls):
        if not ReservationJsonStore.__instance:
            ReservationJsonStore.__instance = ReservationJsonStore.__ReservationJsonStore()
        return ReservationJsonStore.__instance

    '''def find_reservation(self, my_localizer, store_list):
        found = False
        for item in store_list:
            if my_localizer == item["_HotelReservation__localizer"]:
                return item
        raise HotelManagementException("Error: localizer not found")

    def load_reservations_store(self):
        file_store = JSON_FILES_PATH + "store_reservation.json"
        # leo los datos del fichero , si no existe deber dar error porque el almacen de reservaa
        # debe existir para hacer el checkin
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                store_list = json.load(file)
        except FileNotFoundError as exception:
            raise HotelManagementException("Error: store reservation not found") from exception
        except json.JSONDecodeError as exception:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception

        return store_list

'''

