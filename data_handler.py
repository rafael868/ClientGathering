import sqlite3


class DataBase(object):
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

    def InitDb(self):
        self.c.execute("""CREATE TABLE {} (
             name text,
             email text,
             date_of_test text,
             date_of_expire text
        )""".format(self.table_name))
        self.conn.commit()

    def close_conn(self):
        self.conn.close()

    def add_client(self, cl):
        with self.conn:
            self.c.execute("INSERT INTO {} VALUES (?, ?, ?, ?)".format(self.table_name), (cl.name, cl.email,
                                                                                          cl.date_of_test,
                                                                                          cl.date_of_exp))

    def del_clinet(self, name):
        with self.conn:
            self.c.execute("DELETE FROM {} WHERE name=(?)".format(self.table_name), (name,))

    def get_clients(self):
        self.c.execute("SELECT * FROM {}".format(self.table_name))
        return self.c.fetchall()

    def update_name(self, cl, name):
        with self.conn:
            self.c.execute("""UPDATE {} SET ? WHERE email=?""".format(self.table_name), (cl.name,), (cl.email,))


class Client(object):
    def __init__(self):
        self.name = None
        self.email = None
        self.date_of_test = None
        self.date_of_exp = None

    def set_data(self, name, email, date_of_test, date_of_exp):
        self.name = name
        self.email = email
        self.date_of_test = date_of_test
        self.date_of_exp = date_of_exp

    def get_data(self):
        ls = [self.name, self.email, self.date_of_test, self.date_of_exp]
        return ls
