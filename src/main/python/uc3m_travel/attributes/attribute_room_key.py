"Module attribute_room_key"
from .attribute import Attribute

class RoomKey(Attribute):
    "Clase para validar el room_key"
    def __init__(self, room_key):
        self._validation_pattern = r'^[a-fA-F0-9]{64}$'
        self._error_message = "Invalid room key format"
        self._attr_value = self._validate(room_key)
