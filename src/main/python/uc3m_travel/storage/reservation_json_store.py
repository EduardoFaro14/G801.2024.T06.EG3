"Module reservation_json_store"
from .json_store import JsonStore
from ..hotel_management_config import JSON_FILES_PATH
class ReservationJsonStore(JsonStore):
    "Class read, write, add, function 3"
    # pylint: disable=invalid-name
    class __ReservationJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_reservation.json"
        _data_list = []
        _error_message_find = ""

        def add_item(self, my_reservation):
            "Function add, 1"
            self._error_message_find = "Reservation already exists"
            self.find_item("_HotelReservation__localizer", my_reservation.localizer)
            self._error_message_find = "This ID card has another reservation"
            self.find_item("_HotelReservation__id_card", my_reservation.id_card)
            super().add_item(my_reservation)

    __instance = None
    def __new__(cls):
        if not ReservationJsonStore.__instance:
            ReservationJsonStore.__instance = ReservationJsonStore.__ReservationJsonStore()
        return ReservationJsonStore.__instance
