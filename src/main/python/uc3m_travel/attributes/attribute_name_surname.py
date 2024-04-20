from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
class NameSurname(Attribute):
    def __init__(self, name_surname):
        self._validation_pattern = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(name_surname)

    def _validate(self, name_surname):
        super()._validate(name_surname)
        if not name_surname:
            raise HotelManagementException("Invalid name format")
        return name_surname