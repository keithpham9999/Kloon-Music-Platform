import sqlite3

import bcrypt

from Database import Database
from DatabaseError import DatabaseError


class LogInManager(Database):
    def __init__(self):
        """Initialises the database for user
        """
        super().__init__()

    def create_hash(self, password):
        """Forms a hash of the password using a random salt.

            Keyword arguments:
            password -- A string of the password
        """
        # This method creates a hash using a randomly generated salt, two identical passwords will
        # have different hashes
        encoded = str.encode(password)
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(encoded, salt)
        # The hash is returned in bytes not a string
        return hashed

    def confirm_hash(self, password, hash):
        """Checks whether the password matches the hash

            Keyword arguments:
            password -- A string of the password
            hash     -- The hash that the password is being tried against
        """
        try:
            password = str.encode(password)
            print(password)
            print(hash)
            return bcrypt.checkpw(password, hash)
        except TypeError:
            # If the parameter hash is not encoded correctly, i.e a String was passed
            # a type error will be raised
            return False

    def is_valid(self, username, password):
        # Checks whether the username exists in the database and if the password is a match
        """Checks whether the login details are correct

            Keyword arguments:
            username    -- The username to the account
            password    -- The password to the account
        """
        self.execute(f'''
                            SELECT password
                            FROM user
                            WHERE lower(username) = '{username.lower()}'
                            ''')
        data = self.cursor.fetchall()
        if len(data) == 0 or len(data[0]) == 0:
            return False
        return self.confirm_hash(password, data[0][0])

    def fill_user(self):
        """Fills the user table with the first name, last name, username, password
        """
        # This method was required for testing against a database, it will be removed once there is a database
        # set in place
        try:
            self.add_user(1, "Oliver", "Pham", "oliver1999", "qwert123")
            self.add_user(2, "Sub", "Focus", "subfocus4375", "fhsdf456")
        except DatabaseError:
            pass
        self.close()

    def add_user(self, id, first_name, last_name, username, password):
        # Create a new user to be inputted into the user table
        """Adds a new account to the database and assigns them an ID

            Keyword arguments:
            first_name  -- The first name of the new user
            las_name    -- The last name of the new user
            username    -- An unique username for the user
            password    -- The password to the account
        """
        try:
            hash = self.create_hash(password)
            self.cursor.execute(f"INSERT INTO user VALUES(?,?,?,?,?)",
                                (id, first_name, last_name, username, hash))
            self.commit()
        except sqlite3.IntegrityError as e:
            raise DatabaseError(f"Could not add {username} to table -> " + str(e))

    def get_user(self, username):
        """Retrieves the name of the user

            Keyword arguments:
            username    -- The username of the account
        """
        # Get user info
        self.execute(f'''
                            SELECT first_name, last_name, username 
                            FROM user
                            WHERE lower(username) = '{username.lower()}' 
                            ''')
        data = self.cursor.fetchall()

        if len(data) == 0 or len(data[0]) == 0:
            return (["Null", "Null", "Null"])
        return data


