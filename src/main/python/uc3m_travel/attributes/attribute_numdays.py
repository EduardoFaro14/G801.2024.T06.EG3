from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
class NumDays(Attribute):
    def __init__(self, num_days):
        self._validation_pattern = r"^(10|[1-9])$"
        self._error_message = "Invalid numdays format"
        self._attr_value = self._validate(num_days)

    def _validate(self, num_days):
        #super()._validate(num_days)
        try:
            days = int(num_days)
        except ValueError as ex:
            raise HotelManagementException("Invalid num_days datatype") from ex
        if (days < 1 or days > 10):
            raise HotelManagementException("Numdays should be in the range 1-10")
        return num_days
