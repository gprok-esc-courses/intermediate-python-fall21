from contact_list import ContactList


def display_menu():
    print("1. Add")
    print("2. Delete")
    print("3. Search by name")
    print("4. Search by phone")
    print("5. View all")
    print("0. EXIT")


contacts = ContactList()
# Add some contacts
contacts.add("Ann", "123", "a@a.c")
contacts.add("Bill", "111", "b@a.c")
contacts.add("Cathy", "121", "c@a.c")
while True:
    display_menu()
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("email: ")
        contacts.add(name, phone, email)
    elif choice == "2":
        try:
            cid = int(input("ID: "))
            contacts.delete(cid)
        except ValueError:
            print("Invalid ID, must be an integer number")
    elif choice == "3":
        name = input("Name: ")
        contacts.search_by_name(name)
    elif choice == "4":
        phone = input("Phone: ")
        contacts.search_by_phone(phone)
    elif choice == "5":
        contacts.view_catalog()
    elif choice == "0":
        print("bye!")
        break
    else:
        print("Wrong choice. Try again")
