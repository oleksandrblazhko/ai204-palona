from unittest import TestCase
from main import Account

class TestAccount(TestCase):
    def setUp(self):
        self.account = Account("Null")
    def test1(self):
        self.assertTrue(self.account.create_Account("Matvii", "28.11.2002", "+380954841270", "matvii122@gmail.com"))
    def test2(self):
        with self.assertRaises(ValueError, msg="Результат = -1"):
            self.account.create_Account("2atvii", "28.11.2002", "+380954841270", "matvii122@gmail.com")
    def test3(self):
        with self.assertRaises(ValueError, msg="Результат = -1"):
            self.account.create_Account("Maааааааааааtviiіі", "28.11.2002", "+380954841270", "matvii122@gmail.com")
    def test4(self):
        with self.assertRaises(ValueError, msg="Результат = -2"):
            self.account.create_Account("Matvii", "Двадцять восьме.11.2002", "+380954841270", "matvii122@gmail.com")
    def test5(self):
        with self.assertRaises(ValueError, msg="Результат = -3"):
            self.account.create_Account("Matvii", "28.11.2002", "3380954841270", "matvii122@gmail.com")
    def test6(self):
        with self.assertRaises(ValueError, msg="Результат = -3"):
            self.account.create_Account("Matvii", "28.11.2002", "+380954841270000", "matvii122@gmail.com")
    def test7(self):
        with self.assertRaises(ValueError, msg="Результат = -4"):
            self.account.create_Account("Matvii", "28.11.2002", "+380954841270", "matvii122gmail.com")
