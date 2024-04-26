"Module arrival_json_parser"
from uc3m_travel.parser.json_parser import JsonParser

class ArrivalJsonParser(JsonParser):
    "Clase hija parser"
    _JSON_KEYS = ["IdCard", "Localizer"]
    _ERROR_MESSAGE = "Error - Invalid Key in JSON"
