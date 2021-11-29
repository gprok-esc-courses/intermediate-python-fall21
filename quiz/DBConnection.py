import mysql.connector


class DBConnection:
    def __init__(self):
        self.con = mysql.connector.connect(user='root', password='root',
                                      host='127.0.0.1', database='quiz')

    def check_user(self, username):
        pass

    def save_score(self, username, score):
        pass
