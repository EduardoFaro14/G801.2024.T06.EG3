from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
class RoomKey(Attribute):
    def __init__(self, room_key):
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self._validate(room_key)

    def _validate(self, room_key):
        super()._validate(room_key)
        if not room_key:
            raise HotelManagementException("Invalid room key format")
        return room_key