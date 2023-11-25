import unittest
from talaba import Talaba


class TalabaTest(unittest.TestCase):
    """Talaba klasini tekshiramiz"""
    def test_create(self):
        talaba2 = Talaba("Ro'zmetov", "Otabek", 2004, "telekom", "dasturlash", 2, 941_21, 9412203)
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(talaba2.familiya)
        self.assertIsNotNone(talaba2.ism)
        self.assertIsNotNone(talaba2.tyil)
        self.assertIsNotNone(talaba2.fakultet)
        self.assertIsNotNone(talaba2.yonalish)
        self.assertIsNotNone(talaba2.bosqich)
        self.assertIsNotNone(talaba2.guruh)

class ShaxsTest(unittest.TestCase):
    def test_create(self):
        talaba2 = Talaba("Ro'zmetov", "Otabek", 2004, "telekom", "dasturlash", 2, 941_21, 9412203)
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(inson.familiya)
        self.assertIsNotNone(inson.ism)
        self.assertIsNotNone(inson.tyil)
        self.assertIsNotNone(inson.idqaram)
unittest.main()

