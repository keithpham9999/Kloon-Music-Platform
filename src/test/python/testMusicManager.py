import unittest

from src.main.python.DatabaseError import DatabaseError


class TestDatabaseError(unittest.TestCase):
    def setError(self):
        self.databaseError = DatabaseError()

    # Test1
    def testMessage(self):
        message = "Error with the database"
        self.assertEqual(message, "Error with the database", "This should return true for the same message.")

    # Test 2
    def testWrongMessage(self):
        self.assertNotEqual("This is not in error!", "Error with the database",
                            "This should return false for different message.")


if __name__ == '__main__':
    unittest.main()
