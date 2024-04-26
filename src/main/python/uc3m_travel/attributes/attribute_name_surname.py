"Module attribute_name_surname"
from .attribute import Attribute
# pylint: disable=too-few-public-methods
class NameSurname(Attribute):
    "Clase para validar el nombre y apellido(s)"
    def __init__(self, name_surname):
        super().__init__()
        self._validation_pattern = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(name_surname)
