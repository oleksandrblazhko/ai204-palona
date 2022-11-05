class Database:
    def __init__(self, ddatak, ddatab):
        self.ddataK = ddatak
        self.ddataB = ddatab


class Kursinfo:
    def __init__(self, kurs_about, kurs_price):
        self.kurs_about = kurs_about
        self.kurs_price = kurs_price


class Account:
    def __init__(self, aname, abirthday, account_id, aphonenumber, ae_mail):
        self.aname = aname
        self.abirthday = abirthday
        self.account_id = account_id
        self.aphonenumber = aphonenumber
        self.ae_mail = ae_mail


class User(Account, Database, Kursinfo):
    def __init__(self, aname, abirthday, account_id, aphonenumber, ae_mail):
        super().__init__(aname, abirthday, account_id, aphonenumber, ae_mail)

    def review(self):
        return print("\nНазва курсу: ", self.ddataK, "\nОпис курсу: ", self.kurs_about, "\nЦіна курсу: ",
                     self.kurs_price)


class Bezpekainfo:
    def __init__(self, bdocuments):
        self.bdocuments = bdocuments


class assigneeIT:
    def __init__(self, aname, awork):
        self.aname = aname
        self.awork = awork

    def add(self):
        kurs_about = input("Введіть опис курсу: ")
        return print(kurs_about)

    def fixThePrice(self):
        kurs_price = input("Введіть вартість курсу: ")
        return print(kurs_price)


class Administrator(Database, Bezpekainfo, Account):
    def __init__(self, admin_name, ddatak, ddatab):
        super().__init__(ddatak, ddatab)
        self.login = None
        self.password = None
        self.admin_name = admin_name

    def download(self):
        self.ddataK = input("Введіть назву курсу: ")
        self.ddataB = input("Введіть стандарти безпеки праці: ")
        self.bdocuments = input("Введіть нормативні документи: ")

    def analysis(self, *bdocuments):
        print(*bdocuments)

    def protect(self):
        self.login = input("Введіть логін: ")
        self.password = input("Введіть пароль: ")
