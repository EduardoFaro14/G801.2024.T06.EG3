"Module attribute_localizer"
from .attribute import Attribute
# pylint: disable=too-few-public-methods
class Localizer(Attribute):
    "Clase para validar el localizador"
    def __init__(self, localizer):
        super().__init__()
        self._validation_pattern = r'^[a-fA-F0-9]{32}$'
        self._error_message = "Invalid localizer"
        self._attr_value = self._validate(localizer)
