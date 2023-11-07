class User:
    def __init__(self, name, username, email):
        self.name = name
        self.unme = username
        self.mail = email

    def describe(self):
        print(f"sizning ismimngiz{self.name},sizning username giz {self.unme}")

    def get_mail(self):
        print(f" szning gmaulngz {self.mail}")


samuray = User("otabek", "ro'zmetov", "otabek6001218@gamil.com")
print(samuray.describe())
print(samuray.get_mail())
