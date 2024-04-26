"Module attribute_room_key"
from .attribute import Attribute
# pylint: disable=too-few-public-methods
class RoomKey(Attribute):
    "Clase para validar el room_key"
    def __init__(self, room_key):
        super().__init__()
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self._validate(room_key)
