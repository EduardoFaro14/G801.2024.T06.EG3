from uc3m_travel.parser.json_parser import JsonParser

class ArrivalJsonParser(JsonParser):
    _JSON_KEYS = ["IdCard", "Localizer"]
    _ERROR_MESSAGE = "Error - Invalid Key in JSON"