import bcrypt
import sqlite3

# mdp = b"UnSuperMDP"
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(mdp, salt)
# print(hashed)
# print(salt)

# conn = sqlite3.connect("bdd/password.db")
# curs = conn.cursor()
# curs.execute("""CREATE TABLE password (
#                     id INTEGER PRIMARY KEY,
#                     login TEXT NOT NULL,
#                     pwd BLOB NOT NULL UNIQUE,
#                     salt BLOB NOT NULL UNIQUE)""")
# conn.commit()

# curs.execute("INSERT INTO password VALUES (:id, :login, :pwd, :salt)", {'id': 1, 'login': 'tommy', 'pwd': hashed, 'salt': salt})
# conn.commit()

# curs.execute("SELECT * FROM password")
# mdp_bdd = curs.fetchall()[0][2]
# conn.commit()
# print(mdp_bdd)
#
# curs.execute("SELECT * FROM password")
# salt_bdd = curs.fetchall()[0][3]
# conn.commit()
# print(salt_bdd)
#
# mdp = b"UnSuperMDP"
#
# if bcrypt.checkpw(mdp, mdp_bdd):
#     print("true")
# else:
#     print("false")
#
# conn.close()

class DBAccess:

    def __init__(self):
        self.__dbfile = "bdd/password.db"
        self.__connection = None
        self.__cursor = None
        self.__password_table = "password"

    def open(self):
        self.__connection = sqlite3.connect(self.__dbfile)
        self.__cursor = self.__connection.cursor()
