import re
import json
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from ..hotel_management_exception import HotelManagementException
from ..hotel_reservation import HotelReservation
from ..hotel_manager import HotelStay

class JsonStore():

    """_data_list = []
    _file_name = ""
    """

    def __init__(self):
        self._validation_pattern = r""
        self._error_message = ""
        self._attr_value = ""

    """
    def save_list_to_file(self):
    
    def load_list_from_file(self):
    
    def add_item(slf, item):
    
    def find_item(self, key, value):
        self.load_list_from_file()
        for item in self._data_list:
            if item[key] == value:
                return item
        return None
    
    
    
    @property
    def hash(self):
        self.load_store()
        return hashlib.md5(self.__str__().encode()).hexdigest()
    
    
    def save_reservation(self, my_reservation):
        file_store = JSON_FILES_PATH + "store_reservation.json"
    """



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

    def save_checkin(self, my_checkin: HotelStay):
        # escribo el fichero Json con todos los datos
        file_store = JSON_FILES_PATH + "store_check_in.json"

        # leo los datos del fichero si existe , y si no existe creo una lista vacia
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                room_key_list = json.load(file)
        except FileNotFoundError as exception:
            room_key_list = []
        except json.JSONDecodeError as exception:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception

        # comprobar que no he hecho otro ckeckin antes
        for item in room_key_list:
            if my_checkin.room_key == item["_HotelStay__room_key"]:
                raise HotelManagementException("ckeckin  ya realizado")

        # añado los datos de mi reserva a la lista , a lo que hubiera
        room_key_list.append(my_checkin.__dict__)

        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(room_key_list, file, indent=2)
        except FileNotFoundError as exception:
            raise HotelManagementException("Wrong file  or file path") from exception