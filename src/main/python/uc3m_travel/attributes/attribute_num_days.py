"Module attribute_num_days"
from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
# pylint: disable=too-few-public-methods
class NumDays(Attribute):
    "Clase para validar el número de días"
    def __init__(self, num_days):
        super().__init__()
        self._validation_pattern = r"^(10|[1-9])$"
        self._error_message = "Invalid numdays format"
        self._attr_value = self._validate(num_days)

    def _validate(self, _attr_value):
        #super()._validate(num_days)
        try:
            days = int(_attr_value)
        except ValueError as exception:
            raise HotelManagementException("Invalid num_days datatype") from exception
        if (days < 1 or days > 10):
            raise HotelManagementException("Numdays should be in the range 1-10")
        return _attr_value
