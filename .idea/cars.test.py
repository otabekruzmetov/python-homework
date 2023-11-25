# import unittest
# from cars import Car
#
# class CarTest(unittest.TestCase):
#     """car classini tekshirimaiz"""
#
#     def setUp(self):
#         make = "bmw"
#         model = "m8"
#         year = 2020
#         self.price = 40000
#         self.km = 10000
#         self.avto1 = Car(make,model,year)
#         self.avto2 = Car(make,model,year,price=self.price)
#
#     def test_create(self):
#         avto1 = Car("bmw","m8",2020)
#         self.assertIsNotNone(avto1.make)
#         self.assertIsNotNone(avto1.model)
#         self.assertIsNotNone(avto1.year)
#         self.assertIsNone(avto1.price)
#         self.assertEqual(0,avto1.get_km())
#         self.assertEqual(self.price, self.avto2.price)
#
#     def test_set_price(self):
#         self.avto2.set_price(self.price)
#         self.assertEqual(self.price, self.avto2.price)
#
#     def test_add_km(self):
#         # Musbat qiymat berib ko'ramiz
#         self.avto1.add_km(self.km)
#         self.assertEqual(self.km, self.avto1.get_km())
#         # Manfiy qiymat berib ko'ramiz
#         new_km = -5000
#         try:
#             self.avto1.add_km(new_km)
#         except ValueError as error:
#             self.assertEqual(type(error), ValueError)
#
#     def test_get_info(self):
#         avto1_info = 'GM Malibu, 2020-yil, 0km yurgan.'
#         self.assertEqual(avto1_info, self.avto1.get_info())
#         # avto1 narhi va km o'zgartiramiz
#         self.avto1.set_price(50000)
#         self.avto1.add_km(20000)
#         avto1_info = 'GM Malibu, 2020-yil, 20000km yurgan. Narhi: 50000'
#         self.assertEqual(avto1_info, self.avto1.get_info())
# unittest.main()