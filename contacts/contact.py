
class Contact:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
        self.email = ''
        self.phone = ''

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email

    def __str__(self):
        return str(self.cid) + " " + self.name + ", Phone:" + self.phone + ", email:" + self.email


if __name__ == '__main__':
    c = Contact(1, "Peter")
    c.set_phone("8990765431")
    c.set_email("peter@test.xyz")

    print(c)
