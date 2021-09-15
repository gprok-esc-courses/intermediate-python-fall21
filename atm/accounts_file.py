import csv
from account import Account


class AccountsFile:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        accounts = {}
        data_file = open(self.filename)
        csv_reader = csv.reader(data_file, delimiter=',')
        counter = 0
        for row in csv_reader:
            if counter > 0:
                account = Account(row[0], row[1], row[2], int(row[3]))
                accounts[row[0]] = account
                print(account)
            counter += 1
        return accounts

    def save_data(self, accounts):
        data_file = open(self.filename, mode="w")
        csv_writer = csv.writer(data_file, delimiter=',')
        csv_writer.writerow(["account_id", "owners_name", "pin", "balance"])
        for acc_id in accounts:
            csv_writer.writerow(accounts[acc_id].get_csv_row())


if __name__ == '__main__':
    accounts_file = AccountsFile('accounts.csv')
    accounts_file.load_data()
