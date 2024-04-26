"Module json_store"
import json
from ..hotel_management_exception import HotelManagementException
class JsonStore():
    "Class JsonStore"
    _data_list = []
    _file_name = ""
    FILE_PATH = ""
    _error_message_find = ""
    _error_message_not_found = ""
    _error_message_store_not_found = ""

    def __init__(self):
        self.load_list_from_file(self._file_name)

    def save_list_to_file(self, file_store):
        "Function write"
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as exception:
            raise HotelManagementException("Wrong file  or file path") from exception
    def load_list_from_file(self, file_store):
        "Function read new file"
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as exception:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception
        return self._data_list
    def add_item(self, my_reservation):
        "Function add"
        self.load_list_from_file(self._file_name)
        self._data_list.append(my_reservation.__dict__)
        self.save_list_to_file(self._file_name)
    def find_item(self, key, value):
        "Function find"
        self.load_list_from_file(self._file_name)
        for item in self._data_list:
            if item[key] == value:
                raise HotelManagementException(self._error_message_find)
    def return_item(self, key, value):
        "Function find with return item"
        self.load_list_from_file(self._file_name)
        for item in self._data_list:
            if item[key] == value:
                return item
        return None

    def read_store(self):
        "Function read not new files"
        try:
            with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError as exception:
            raise HotelManagementException(self._error_message_store_not_found) from exception
        except json.JSONDecodeError as exception:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception
        return self._data_list
