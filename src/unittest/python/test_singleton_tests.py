"Module test of singleton"
import unittest
from uc3m_travel import HotelManager
from uc3m_travel.storage.reservation_json_store import ReservationJsonStore
from uc3m_travel.storage.stay_json_store import StayJsonStore
from uc3m_travel.storage.checkout_json_store import CheckOutJsonStore

class MyTestCase(unittest.TestCase):
    "Tests singleton"
    def test_hotel_manager(self):
        "Test singleton hotel_manager"
        mi_primera_instancia = HotelManager()
        mi_segunda_instancia = HotelManager()
        self.assertEqual(mi_primera_instancia, mi_segunda_instancia)

    def test_reservation_json_store(self):
        "Test singleton reservation_json_store"
        mi_primera_instancia = ReservationJsonStore()
        mi_segunda_instancia = ReservationJsonStore()
        self.assertEqual(mi_primera_instancia, mi_segunda_instancia)

    def test_stay_json_store(self):
        "Test singleton stay_json_store"
        mi_primera_instancia = StayJsonStore()
        mi_segunda_instancia = StayJsonStore()
        self.assertEqual(mi_primera_instancia, mi_segunda_instancia)

    def test_checkout_json_store(self):
        "Test singleton checkout_json_store"
        mi_primera_instancia = CheckOutJsonStore()
        mi_segunda_instancia = CheckOutJsonStore()
        self.assertEqual(mi_primera_instancia, mi_segunda_instancia)

if __name__ == '__main__':
    unittest.main()
