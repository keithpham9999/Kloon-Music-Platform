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

    def create_login_tables(self):
        """Constructs the tables used for the login system
        """
        self.execute(
            '''CREATE TABLE IF NOT EXISTS roles(
            role_id SERIAL  PRIMARY KEY,
            role_name       VARCHAR(16) NOT NULL, 
            role_desc       VARCHAR(512) NOT NULL
            )''')

        self.execute(
            '''CREATE TABLE IF NOT EXISTS staff(
            staff_id SERIAL PRIMARY KEY,
            first_name      VARCHAR(16) NOT NULL, 
            last_name       VARCHAR(16) NOT NULL,
            username        VARCHAR(16) UNIQUE NOT NULL,
            password        VARCHAR(32) NOT NULL,
            role_id         SERIAL NOT NULL
            )''')
        self.commit()

    def create_music_tables(self):
        """Constructs the tables used for storing music system
        """

        self.execute(
            '''CREATE TABLE IF NOT EXISTS music(
            track_id SERIAL PRIMARY KEY,
            track_source     VARCHAR(16) NOT NULL,
            track_name      VARCHAR(16) NOT NULL, 
            artist_name       VARCHAR(16) NOT NULL,
            genre        VARCHAR(16) NOT NULL
            )''')
        self.commit()

    def fill_music(self):
        """Fills the music table with the tracks
        """
        # This method was required for testing against a database, it will be removed once there is a database
        # set in place
        try:
            self.execute("INSERT INTO music values(1, 'music/4B x Junkie Kid - Love Is Dead.mp3','Love Is Dead',"
                         "'4B, Junkie K', 'Hardstyle')")
            self.execute("INSERT INTO music values(2, 'Chef', 'N/A')")
            self.execute("INSERT INTO music values(3, 'Manager', 'N/A')")
            self.commit()
        except:
            pass

    def music_reset(self):
        self.create_music_tables()

    def close(self):
        """Terminates the connection to the database
        """
        self.conn.close()