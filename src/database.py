import bcrypt
import sqlite3



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
