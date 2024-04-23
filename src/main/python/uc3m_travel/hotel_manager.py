"""Module for the hotel manager"""
import re
import json
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from freezegun import freeze_time
from .attributes.attribute_localizer import Localizer
from .attributes.attribute_idcard import IdCard
from .storage.json_store import JsonStore
from .storage.reservation_json_store import ReservationJsonStore
from .storage.stay_json_store import StayJsonStore


class HotelManager:
    class __HotelManager:
        """Class with all the methods for managing reservations and stays"""
        def __init__(self):
            pass
        def read_data_from_json(self, fi):
            """reads the content of a json file with two fields: CreditCard and phoneNumber"""
            try:
                with open(fi, encoding='utf-8') as file:
                    json_data = json.load(file)
            except FileNotFoundError as exception:
                raise HotelManagementException("Wrong file or file path") from exception
            except json.JSONDecodeError as exception:
                raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception
            try:
                credit_card = json_data["CreditCard"]
                phone_number = json_data["phoneNumber"]
                data = HotelReservation(id_card="12345678Z",
                                       credit_card_number=credit_card,
                                       name_surname="John Doe",
                                       phone_number=phone_number,
                                       room_type="single",
                                       num_days=3,
                                       arrival="20/01/2024")
            except KeyError as exception:
                raise HotelManagementException("JSON Decode Error - Invalid JSON Key") from exception
            #if not self.validatecreditcard(c):
                #raise HotelManagementException("Invalid credit card number")
            # Close the file
            return data

        # pylint: disable=too-many-arguments
        def room_reservation(self,
                             credit_card:str,
                             name_surname:str,
                             id_card:str,
                             phone_number:str,
                             room_type:str,
                             arrival_date: str,
                             num_days:int)->str:
            """manges the hotel reservation: creates a reservation and saves it into a json file"""
            my_reservation = HotelReservation(id_card=id_card,
                                              credit_card_number=credit_card,
                                              name_surname=name_surname,
                                              phone_number=phone_number,
                                              room_type=room_type,
                                              arrival=arrival_date,
                                              num_days=num_days)
            reservation_store = ReservationJsonStore()
            reservation_store.add_item(my_reservation)

            return my_reservation.localizer

        def guest_arrival(self, file_input:str)->str:
            """manages the arrival of a guest with a reservation"""
            try:
                with open(file_input, "r", encoding="utf-8", newline="") as file:
                    input_list = json.load(file)
            except FileNotFoundError as exception:
                raise HotelManagementException ("Error: file input not found") from exception
            except json.JSONDecodeError as exception:
                raise HotelManagementException ("JSON Decode Error - Wrong JSON Format") from exception

            # comprobar valores del fichero
            try:
                my_localizer = Localizer(input_list["Localizer"]).value
                my_id_card = IdCard(input_list["IdCard"]).value
            except KeyError as exception:
                raise HotelManagementException("Error - Invalid Key in JSON") from exception

            self.validate_id_card(my_id_card)

            self.validate_localizer(my_localizer)

            #buscar en almacen
            reservation_data = self.find_reservation(my_id_card, my_localizer)

            #reservation_credit_card, reservation_date_arrival, reservation_date_timestamp, reservation_days, reservation_id_card, reservation_name, reservation_phone, reservation_room_type = self.find_reservation(
                #my_id_card, my_localizer)

            # regenrar clave y ver si coincide
            reservation_date = datetime.fromtimestamp(reservation_data["_HotelReservation__reservation_date"])

            with freeze_time(reservation_date):
                new_reservation = HotelReservation(credit_card_number=reservation_credit_card,
                                                   id_card=reservation_id_card,
                                                   num_days=reservation_days,
                                                   room_type=reservation_room_type,
                                                   arrival=reservation_date_arrival,
                                                   name_surname=reservation_name,
                                                   phone_number=reservation_phone)
            if new_reservation.localizer != my_localizer:
                raise HotelManagementException("Error: reservation has been manipulated")

            # compruebo si hoy es la fecha de checkin
            reservation_format = "%d/%m/%Y"
            date_obj = datetime.strptime(reservation_date_arrival, reservation_format)
            if date_obj.date()!= datetime.date(datetime.utcnow()):
                raise HotelManagementException("Error: today is not reservation date")

            # genero la room key para ello llamo a Hotel Stay
            my_checkin = HotelStay(idcard=my_id_card, numdays=int(reservation_days),
                                   localizer=my_localizer, roomtype=reservation_room_type)

            #Ahora lo guardo en el almacen nuevo de checkin
            reservation_store = JsonStore()
            reservation_store.save_checkin(my_checkin)

            stay_store = StayJsonStore()
            stay_store.add_item(my_checkin)
            '''# escribo el fichero Json con todos los datos
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
                    raise HotelManagementException ("ckeckin  ya realizado")
    
            #añado los datos de mi reserva a la lista , a lo que hubiera
            room_key_list.append(my_checkin.__dict__)
    
            try:
                with open(file_store, "w", encoding="utf-8", newline="") as file:
                    json.dump(room_key_list, file, indent=2)
            except FileNotFoundError as exception:
                raise HotelManagementException("Wrong file  or file path") from exception'''

            return my_checkin.room_key

        def find_reservation(self, my_id_card, my_localizer):
            file_store = JSON_FILES_PATH + "store_reservation.json"
            # leo los datos del fichero , si no existe deber dar error porque el almacen de reservaa
            # debe existir para hacer el checkin
            try:
                with open(file_store, "r", encoding="utf-8", newline="") as file:
                    store_list = json.load(file)
            except FileNotFoundError as exception:
                raise HotelManagementException("Error: store reservation not found") from exception
            except json.JSONDecodeError as exception:
                raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception
            # compruebo si esa reserva esta en el almacen
            found = False
            for item in store_list:
                if my_localizer == item["_HotelReservation__localizer"]:
                    reservation_days = item["_HotelReservation__num_days"]
                    reservation_room_type = item["_HotelReservation__room_type"]
                    reservation_date_timestamp = item["_HotelReservation__reservation_date"]
                    reservation_credit_card = item["_HotelReservation__credit_card_number"]
                    reservation_date_arrival = item["_HotelReservation__arrival"]
                    reservation_name = item["_HotelReservation__name_surname"]
                    reservation_phone = item["_HotelReservation__phone_number"]
                    reservation_id_card = item["_HotelReservation__id_card"]
                    found = True
            if not found:
                raise HotelManagementException("Error: localizer not found")
            if my_id_card != reservation_id_card:
                raise HotelManagementException("Error: Localizer is not correct for this IdCard")
            return reservation_credit_card, reservation_date_arrival, reservation_date_timestamp, reservation_days, reservation_id_card, reservation_name, reservation_phone, reservation_room_type

        def guest_checkout(self, room_key:str)->bool:
            """manages the checkout of a guest"""
            #self.validate_roomkey(room_key)
            #check thawt the roomkey is stored in the checkins file
            file_store = JSON_FILES_PATH + "store_check_in.json"
            try:
                with open(file_store, "r", encoding="utf-8", newline="") as file:
                    room_key_list = json.load(file)
            except FileNotFoundError as exception:
                raise HotelManagementException("Error: store checkin not found") from exception
            except json.JSONDecodeError as exception:
                raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception

            # comprobar que esa room_key es la que me han dado
            found = False
            for item in room_key_list:
                if room_key == item["_HotelStay__room_key"]:
                    departure_date_timestamp = item["_HotelStay__departure"]
                    found = True
            if not found:
                raise HotelManagementException ("Error: room key not found")

            today = datetime.utcnow().date()
            if datetime.fromtimestamp(departure_date_timestamp).date() != today:
                raise HotelManagementException("Error: today is not the departure day")

            file_store_checkout = JSON_FILES_PATH + "store_check_out.json"
            try:
                with open(file_store_checkout, "r", encoding="utf-8", newline="") as file:
                    room_key_list = json.load(file)
            except FileNotFoundError as exception:
                room_key_list = []
            except json.JSONDecodeError as exception:
                raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from exception

            for checkout in room_key_list:
                if checkout["room_key"] == room_key:
                    raise HotelManagementException("Guest is already out")

            room_checkout={"room_key":  room_key, "checkout_time":datetime.timestamp(datetime.utcnow())}

            room_key_list.append(room_checkout)

            try:
                with open(file_store_checkout, "w", encoding="utf-8", newline="") as file:
                    json.dump(room_key_list, file, indent=2)
            except FileNotFoundError as exception:
                raise HotelManagementException("Wrong file  or file path") from exception

            return True

    __instance = None
    def __new__(cls):
        if not HotelManager.__instance:
            HotelManager.__instance = HotelManager.__HotelManager()
        return HotelManager.__instance
