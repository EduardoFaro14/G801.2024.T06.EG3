import re
import json
from .. import JSON_FILES_PATH
from ..hotel_management_exception import HotelManagementException
from ..hotel_reservation import HotelReservation

class JsonStore():
    def __init__(self):
        self._validation_pattern = r""
        self._error_message = ""
        self._attr_value = ""

    def save_reservation(self, reservation_data: HotelReservation):
        file_store = JSON_FILES_PATH + "store_reservation.json"

        # leo los datos del fichero si existe , y si no existe creo una lista vacia
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as exception:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception

        # compruebo que esta reserva no esta en la lista
        for item in data_list:
            if reservation_data.localizer == item["_HotelReservation__localizer"]:
                raise HotelManagementException("Reservation already exists")
            if reservation_data.id_card == item["_HotelReservation__id_card"]:
                raise HotelManagementException("This ID card has another reservation")
        # añado los datos de mi reserva a la lista , a lo que hubiera
        data_list.append(reservation_data.__dict__)

        # escribo la lista en el fichero
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as exception:
            raise HotelManagementException("Wrong file  or file path") from exception