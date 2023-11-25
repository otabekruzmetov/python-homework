import unittest
from test import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon','valiyev')
        self.assertEqual(formatted_name, 'Alijon Valiyev')
    def test_toliq_ism_otasi(self):
        test = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(test,'Hasan Olimovich Husanov')

unittest.main()

