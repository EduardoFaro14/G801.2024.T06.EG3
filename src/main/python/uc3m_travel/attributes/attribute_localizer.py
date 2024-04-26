"Module attribute_localizer"
from .attribute import Attribute
class Localizer(Attribute):
    "Clase para validar el localizador"
    def __init__(self, localizer):
        self._validation_pattern = r'^[a-fA-F0-9]{32}$'
        self._error_message = "Invalid localizer"
        self._attr_value = self._validate(localizer)
