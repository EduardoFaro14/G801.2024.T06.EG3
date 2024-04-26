"Module stay_json_store"
from ..hotel_management_config import JSON_FILES_PATH
from .json_store import JsonStore
class StayJsonStore(JsonStore):
    "Class add, read, write, function 2"
    # pylint: disable=invalid-name
    class __StayJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_check_in.json"
        _error_message_store_not_found = "Error: store checkin not found"
        _error_message_find = "ckeckin ya realizado"

        def add_item(self, my_reservation):
            "Function add"
            self.find_item("room_key", my_reservation.room_key)
            super().add_item(my_reservation)

    __instance = None
    def __new__(cls):
        if not StayJsonStore.__instance:
            StayJsonStore.__instance = StayJsonStore.__StayJsonStore()
        return StayJsonStore.__instance
