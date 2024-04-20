from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
class RoomType(Attribute):
    def __init__(self, room_type):
        self._validation_pattern = r"(SINGLE|DOUBLE|SUITE)"
        self._error_message = "Invalid roomtype value"
        self._attr_value = self._validate(room_type)

    def _validate(self, room_type):
        super()._validate(room_type)
        if not room_type:
            raise HotelManagementException("Invalid roomtype value")
        return room_type