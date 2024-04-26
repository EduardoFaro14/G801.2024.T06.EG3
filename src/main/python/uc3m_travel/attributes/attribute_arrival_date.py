"Module attribute_arrival_date"
from .attribute import Attribute
class ArrivalDate(Attribute):
    "Clase para validar la fecha de llegada"
    def __init__(self, arrival_date):
        self._validation_pattern = r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$"
        self._error_message = "Invalid date format"
        self._attr_value = self._validate(arrival_date)
