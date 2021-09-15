
class Account:
    def __init__(self, acc_id, owner, pin, balance):
        self.acc_id = acc_id
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def get_csv_row(self):
        return [self.acc_id, self.owner, self.pin, self.balance]

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def is_valid_pin(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    def __str__(self):
        return "Account " + self.acc_id + ", " + self.owner

