from accounts_file import AccountsFile


class Bank:
    def __init__(self):
        self.accounts_file = AccountsFile('accounts.csv')
        self.accounts = self.accounts_file.load_data()
        self.acc_id = None
        self.pin = None

    def login_form(self):
        acc_id = input("Account ID: ")
        if acc_id == "0":
            return True
        if acc_id in self.accounts:
            pin = input("PIN: ")
            if self.accounts[acc_id].is_valid_pin(pin):
                self.acc_id = acc_id
                self.pin = pin
            else:
                print("Wrong PIN")
        else:
            print("Invalid account ID")
        return False

    def bank_menu(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("0. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            amount = int(input("Amount to deposit: "))
            if not self.accounts[self.acc_id].deposit(amount):
                print("Invalid deposit amount")
        elif choice == "2":
            amount = int(input("Amount to deposit: "))
            if not self.accounts[self.acc_id].withdraw(amount):
                print("Invalid withdraw amount")
        elif choice == "3":
            print("Balance: ", self.accounts[self.acc_id].get_balance())
            pass
        elif choice == "0":
            self.logout()
            pass
        else:
            print("Wrong choice")
        return choice

    def logout(self):
        self.acc_id = None
        self.pin = None

    def run_atm(self):
        while True:
            terminate = self.login_form()
            if terminate:
                self.accounts_file.save_data(self.accounts)
                break
            if self.acc_id is not None:
                while True:
                    choice = self.bank_menu()
                    if choice == "0":
                        break


if __name__ == '__main__':
    bank = Bank()
    bank.run_atm()