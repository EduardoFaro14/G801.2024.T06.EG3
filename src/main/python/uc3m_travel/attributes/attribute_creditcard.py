from .attribute import Attribute
from ..hotel_management_exception import HotelManagementException
class CreditCard(Attribute):
    def __init__(self, credit_card):
        self._validation_pattern = r"^[0-9]{16}"
        self._error_message = "Invalid CreditCard format"
        self._attr_value = self._validate(credit_card)

    def _validate(self, credit_card):
        super()._validate(credit_card)
        def digits_of(n):
            return [int(d) for d in str(n)]


        digits = digits_of(credit_card)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        if not checksum % 10 == 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")
        return credit_card