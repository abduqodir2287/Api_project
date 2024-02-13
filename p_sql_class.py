import psycopg2
from config import db_name, user, password, host

class helperDB:

    def __init__(self, dbname='tech.db'):
        con = psycopg2.connect(password=password, user=user, host=host, port=5432, dbname=db_name)
        self.dbname = dbname
        self.tabname = ''
        self.conn = con
        self.cur = con.cursor()

    def setup(self, tabname='custom'):
        """
        create table for database
        :param tabname: base name
        :return: default table name id, username
        """
        self.tabname = tabname
        sql = f"""
                CREATE TABLE IF NOT EXISTS {tabname}(
                      id SERIAL PRIMARY KEY,
                      "userID" INTEGER,
                      "username" TEXT
                    );"""

        self.cur.execute(sql)
        self.conn.commit()

    def add_item(self, userID: int, username: str):
        sql = f"""INSERT INTO "{self.tabname}" ("userID", "username")
            VALUES (%s, %s);"""
        data = (userID, username)
        self.cur.execute(sql, data)
        self.conn.commit()

    def delete_item(self, id):
        sql = f"""DELETE FROM {self.tabname} where id = %s;"""
        self.cur.execute(sql, (id,))
        self.conn.commit()

    def select_item(self):
        sql = f"""SELECT * FROM {self.tabname};"""
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update_item(self, id, username):
        sql = f"""UPDATE {self.tabname} SET 
                "username" = %s 
                WHERE id = %s;"""
        data = (username, id)
        self.cur.execute(sql, data)
        self.conn.commit()

    def log_out(self):
        self.cur.close()
        self.conn.close()
