"Module attribute_phone_number"
from .attribute import Attribute
# pylint: disable=too-few-public-methods
class PhoneNumber(Attribute):
    "Clase para validar el número de teléfono"
    def __init__(self, phone_number):
        super().__init__()
        self._validation_pattern = r"^(\+)[0-9]{9}"
        self._error_message = "Invalid phone number format"
        self._attr_value = self._validate(phone_number)
