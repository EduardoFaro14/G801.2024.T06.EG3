"Module attribute_credit_card"
from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
# pylint: disable=too-few-public-methods
class CreditCard(Attribute):
    "Clase para validar la tarjeta de crédito"
    def __init__(self, credit_card):
        super().__init__()
        self._validation_pattern = r"^[0-9]{16}"
        self._error_message = "Invalid credit card format"
        self._attr_value = self._validate(credit_card)

    def _validate(self, _attr_value):
        super()._validate(_attr_value)
        def digits_of(number):
            return [int(digits) for digits in str(number)]


        digits = digits_of(_attr_value)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for digit in even_digits:
            checksum += sum(digits_of(digit * 2))
        if not checksum % 10 == 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")
        return _attr_value
