from ..hotel_management_exception import HotelManagementException
import json
class JsonParser():
    _JSON_KEYS = []
    _ERROR_MESSAGE = "JSON Decode Error - Wrong JSON Format"
    _json_content = None

    def __init__(self, input_file):
        self._input_file = input_file
        self._json_content = self.load_json_content()
        self.validate_json_keys()

    def validate_json_keys(self):
        for key in self._JSON_KEYS:
            if key not in self._json_content.keys():
                raise HotelManagementException(self._ERROR_MESSAGE)

    def load_json_content(self):
        """Loads the content of the json file in a dictionary"""
        try:
            with open(self._input_file, "r", encoding="utf-8", newline="") as file:
                data = json.load(file)
        except FileNotFoundError as ex:
            raise HotelManagementException("File is not found") from ex
        except json.JSONDecodeError as ex:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from ex
        return data

    @property
    def json_content(self):
        return self._json_content