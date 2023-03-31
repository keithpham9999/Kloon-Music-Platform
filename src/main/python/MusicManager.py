import sqlite3

from Database import Database

#from src.main.python.Database import Database

class MusicManager(Database):
    def __init__(self):
        """Initialises database and add tables
        """
        super().__init__()
        self.fill_music()

    def get_music(self):
        """Retrieves all the music from music table
        """
        # Get the different types of food
        self.execute("SELECT * FROM music")
        data = self.cursor.fetchall()
        return data

    def clear(self):
        """Refreshes all music tables
        """
        self.execute("DROP table IF EXISTS music")
        self.commit()
        self.create_music_tables()


