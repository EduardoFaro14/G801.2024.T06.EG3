"Module attribute_num_days"
from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
# pylint: disable=too-few-public-methods
class NumDays(Attribute):
    "Clase para validar el número de días"
    def __init__(self, num_days):
        super().__init__()
        self._validation_pattern = r"^[0-9]*$"
        self._error_message = "Invalid num_days datatype"
        self._attr_value = self._validate(num_days)

    def _validate(self, _attr_value):
        super()._validate(str(_attr_value))
        if (_attr_value < 1 or _attr_value > 10):
            raise HotelManagementException("Numdays should be in the range 1-10")
        return _attr_value
