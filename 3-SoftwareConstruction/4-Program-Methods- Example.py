# Мова програмування Python
class Database:
    def __init__(self, ddatak, ddatab):
        self.ddataK = ddatak
        self.ddataB = ddatab


class Kursinfo:
    def __init__(self, kurs_about, kurs_price):
        self.kurs_about = kurs_about
        self.kurs_price = kurs_price


class Account:
    def create_Account(self): # Метод введення створення акаунту
        aname = input("Введіть ім'я: ")
        abirthday = input("Введіть дату народження: ")
        aphonenumber = input("Введіть номер телефону: ")
        ae_mail = input("Введіть електрону адресу: ")
        return aname, abirthday, aphonenumber, ae_mail
        print("Аккаунт створено")

    def __init__(self, account_id, aname, abirthday, aphonenumber, ae_mail):
        self.aname = aname
        self.abirthday = abirthday
        self.account_id = account_id
        self.aphonenumber = aphonenumber
        self.ae_mail = ae_mail


class User(Account, Database, Kursinfo):
    def __init__(self, aname, abirthday, account_id, aphonenumber, ae_mail):
        super().__init__(aname, abirthday, account_id, aphonenumber, ae_mail)

    def review(self): # Метод перегляду інформації про курс
        return print("\nНазва курсу: ", self.ddataK, "\nОпис курсу: ", self.kurs_about, "\nЦіна курсу: ", self.kurs_price)
