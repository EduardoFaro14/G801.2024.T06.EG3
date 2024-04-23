import unittest
from uc3m_travel import HotelManager
from uc3m_travel.storage import ReservationJsonStore

class MyTestCase(unittest.TestCase):
    def test_something(self):
        mi_primera_instancia = HotelManager()
        mi_segunda_instancia = HotelManager()
        self.assertEqual(mi_primera_instancia, mi_segunda_instancia)  # add assertion here
    def test_something(self):
        mi_primera_instancia = ReservationJsonStore()
        mi_segunda_instancia = HotelManager()
        self.assertEqual(mi_primera_instancia, mi_segunda_instancia)  # add assertion here

if __name__ == '__main__':
    unittest.main()
