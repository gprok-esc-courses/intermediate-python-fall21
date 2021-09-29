from contact import Contact


class ContactList:
    def __init__(self):
        self.contacts = {}
        self.next_id = 1

    def add(self, name, phone, email):
        c = Contact(self.next_id, name)
        c.set_email(email)
        c.set_phone(phone)
        self.contacts[self.next_id] = c
        self.next_id += 1

    def view_catalog(self):
        for cid in self.contacts:
            print(self.contacts[cid])

    def search_by_name(self, name):
        for cid in self.contacts:
            if self.contacts[cid].name == name:
                print(self.contacts[cid])

    def search_by_phone(self, phone):
        for cid in self.contacts:
            if self.contacts[cid].phone == phone:
                print(self.contacts[cid])

    def delete(self, cid):
        if cid in self.contacts:
            del self.contacts[cid]
            print("Contact deleted!")
        else:
            print("ID not found")



if __name__ == '__main__':
    cat = ContactList()
    cat.add("Peter", "", "a@v.c")
    cat.add("John", "234", "j@v.c")
    cat.view_catalog()

