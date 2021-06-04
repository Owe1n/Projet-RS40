import bcrypt
import sqlite3

# mdp = b"UnSuperMDP"
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(mdp, salt)
# print(hashed)
# print(salt)

# conn = sqlite3.connect("bdd/password.db")
# curs = conn.cursor()
# curs.execute("SELECT max(id) FROM password")
# if curs.fetchone()[0] is None:
#     print("pas de valeurs")
# conn.commit()
# curs.execute("DROP TABLE password")
# conn.commit()
# curs.execute("""CREATE TABLE password (
#                     id INTEGER PRIMARY KEY,
#                     login TEXT NOT NULL UNIQUE,
#                     pwd BLOB NOT NULL UNIQUE,
#                     salt BLOB NOT NULL UNIQUE)""")
# conn.commit()
#
# curs.execute("INSERT INTO password VALUES (:id, :login, :pwd, :salt)", {'id': 2, 'login': 'owein', 'pwd': hashed, 'salt': salt})
# conn.commit()

# curs.execute("SELECT * FROM password")
# print(curs.fetchall())
# conn.commit()
# mdp_bdd = curs.fetchall()[0][2]
# conn.commit()
# print(mdp_bdd)
#
# mdp = bytes("UnSuperMDP", encoding='utf-8')
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

    def __open(self):
        self.__connection = sqlite3.connect(self.__dbfile)
        self.__cursor = self.__connection.cursor()

    def __verif_login_does_not_exist(self, login):
        self.__cursor.execute("SELECT login FROM password")
        tuples = self.__cursor.fetchall()
        self.__connection.commit()
        for t in tuples:
            log = t[0]
            if login == log:
                return -1
        return 0

    def __verif_pwd_does_not_exist(self, password):
        self.__cursor.execute("SELECT pwd FROM password")
        tuples = self.__cursor.fetchall()
        self.__connection.commit()
        for t in tuples:
            pwd = t[0]
            if bcrypt.checkpw(bytes(password, encoding='utf-8'), pwd):
                return -1
        return 0

    def __verif_salt_does_not_exist(self, salt):
        self.__cursor.execute("SELECT salt FROM password")
        tuples = self.__cursor.fetchall()
        self.__connection.commit()
        for t in tuples:
            s = t[0]
            if salt == s:
                return -1
        return 0

    def sign_up(self, login, password):
        self.__open()
        if self.__verif_login_does_not_exist(login) != 0:
            self.__close()
            return 1

        self.__cursor.execute("SELECT max(id) FROM password")
        max_id = self.__cursor.fetchone()[0]
        self.__connection.commit()
        if max_id is None:
            max_id = -1
        salt = bcrypt.gensalt()
        while self.__verif_salt_does_not_exist(salt) != 0:
            salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(bytes(password, encoding='utf-8'), salt)

        self.__cursor.execute("INSERT INTO password VALUES (:id, :login, :pwd, :salt)", {'id': max_id+1, 'login': login, 'pwd': hashed, 'salt': salt})
        self.__connection.commit()

        self.__close()
        return 0

    def sign_in(self, login, password):
        self.__open()
        if self.__verif_login_does_not_exist(login) == 0:
            self.__close()
            return 1
        self.__cursor.execute("SELECT pwd FROM password WHERE login = :login", {'login': login})
        pwd = self.__cursor.fetchone()[0]
        self.__connection.commit()
        if bcrypt.checkpw(bytes(password, encoding='utf-8'), pwd):
            self.__close()
            return 0
        else:
            self.__close()
            return 2

    def __close(self):
        self.__connection.close()


if __name__ == '__main__':
    dbaccess = DBAccess()
    # res = dbaccess.sign_up("theo", "lafamosa")
    # if res == 0:
    #     print("Création de compte réussi")
    # else:
    #     print("Login deja pris")
    # dbaccess.sign_up("owein", "lafamosa")
    # res = dbaccess.sign_in("theo", "lafamosa")
    # if res == 0:
    #     print("Connexion réussi")
    # elif res == 1:
    #     print("Login inexistant")
    # else:
    #     print("Mot de passe incorrect")

    conn = sqlite3.connect("bdd/password.db")
    curs = conn.cursor()
    # curs.execute("delete from password")
    # conn.commit()
    curs.execute("select * from password")
    print(curs.fetchall())
    conn.commit()
    conn.close()