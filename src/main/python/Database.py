import os
import sqlite3

class Database:
    def __init__(self):
        """Initialises the connection to the database
        """
        # generate absolute path of file
        address = "src/main/resources/kloon.db"
        ad = os.path.abspath(address)
        self.conn = sqlite3.connect(ad)
        self.cursor = self.conn.cursor()
        self.create_tables()

        self.fill_roles()
        self.fill_types()
        self.assign_status()

    def execute(self, query, vars=""):
        """Executes the query

            Keyword arguments:
            query       -- A SQL query
        """
        self.cursor.execute(query, vars)

    def commit(self):
        """Writes any changes to the database
        """
        self.conn.commit()

    def fetchall(self):
        """Retrieves all data gathered since the last query
        """
        return self.cursor.fetchall()

    def create_tables(self):
        """Constructs the tables for the database
        """
        self.create_login_tables()
        self.create_menu_tables()
        self.create_order_tables()

    def close(self):
        """Terminates the connection to the database
        """
        self.conn.close()