"Module checkout_json_store"
from ..hotel_management_config import JSON_FILES_PATH
from .json_store import JsonStore

class CheckOutJsonStore(JsonStore):
    "Class read, write, add, function 3"
    # pylint: disable=invalid-name
    class __CheckOutJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_check_out.json"
        _error_message_store_not_found = "Error: file input not found"
        _error_message_find = "Guest is already out"

        def add_item(self, my_reservation):
            self.find_item("room_key", my_reservation.room_key)
            super().add_item(my_reservation)

    __instance = None
    def __new__(cls):
        if not CheckOutJsonStore.__instance:
            CheckOutJsonStore.__instance = CheckOutJsonStore.__CheckOutJsonStore()
        return CheckOutJsonStore.__instance
