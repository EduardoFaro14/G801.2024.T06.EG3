from ..hotel_management_config import JSON_FILES_PATH
from .json_store import JsonStore

class StayJsonStore(JsonStore):
    class __StayJsonStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_check_in.json"
        _file_name2 = JSON_FILES_PATH + "store_reservation.json"
        _error_message_store_not_found = "Error: file input not found"
        _error_message_find = "ckeckin  ya realizado"

        def add_item(self, item):
            self.find_item("room_key", item.room_key)
            super().add_item(item)

    def __new__(cls):
        if not StayJsonStore.__instance:
            StayJsonStore.__instance = StayJsonStore.__StayJsonStore()
        return StayJsonStore.__instance