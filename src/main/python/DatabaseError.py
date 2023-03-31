class DatabaseError(Exception):
    # Class to wrap the different exceptions into one class
    def __init__(self, message="Error with the database"):
        """Creates an exception with a message

            Keyword arguments:
            message         -- A message to describe the error
        """
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Retrieves the error message
        """
        return self.message
