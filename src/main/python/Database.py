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

        self.create_music_tables()
        self.fill_music()

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


    def create_music_tables(self):
        """Constructs the tables used for storing music system
        """

        self.execute(
            '''CREATE TABLE IF NOT EXISTS music(
            track_id  INT PRIMARY KEY,
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
            self.execute("INSERT INTO music values(1, '4B x Junkie Kid - Love Is Dead.mp3','Love Is Dead',"
                         "'4B, Junkie K', 'Hardstyle')")
            self.commit()
        except sqlite3.IntegrityError:
            pass


    def music_reset(self):
        """Resets the music table
        """
        self.execute("DROP table IF EXISTS music")
        self.commit()
        self.drop_sqlite_master()
        self.create_music_tables()
        self.fill_music()

    def close(self):
        """Terminates the connection to the database
        """
        self.conn.close()
