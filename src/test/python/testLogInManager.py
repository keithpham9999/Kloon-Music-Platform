import unittest

import src.main.python.LogInManager as login


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login = login.LogInManager()
        self.login.user_reset()
        self.login.fill_user()

    def tearDown(self):
        self.login.close()

    def testCreateHash(self):
        # Test 1 ensuring the function is returning something other than the password
        password = "1234"
        self.assertNotEqual(password, self.login.create_hash(password))

    def testCreateHashDifferent(self):
        # Test 2 ensuring the hash returned is different for different password
        password1 = "1234"
        password2 = "1235"
        hash1 = self.login.create_hash(password1)
        hash2 = self.login.create_hash(password2)
        self.assertNotEqual(hash1, hash2)

    def testSalting(self):
        # Test 3 is to check that the same password will generate different hashes because of salting
        password = "1234"
        hash1 = self.login.create_hash(password)
        hash2 = self.login.create_hash(password)
        self.assertNotEqual(hash1, hash2)

    def testConfirmPassword(self):
        # Test 4 check that the hash can be confirmed
        password = "1234"
        hash = self.login.create_hash(password)
        self.assertTrue(self.login.confirm_hash(password, hash))

    def testConfirmPasswordIncorrect(self):
        # Test 5 check that the hash can be confirmed
        password = "1234"
        hash = self.login.create_hash(password)
        self.assertFalse(self.login.confirm_hash(password + "wrong", hash))

    def testWrongEncoding(self):
        # Test 6 ensuring an exception is caught
        password = "qwert"
        self.assertFalse(self.login.confirm_hash(password, "WrongHash"))

    def testValidateAdmin(self):
        # Test 7 checks that the login can validate a user
        id = 3
        first_name = "Mike"
        last_name = "Killer"
        password = "qwert123"
        username = "mikey4567"
        self.login.add_user(id, first_name, last_name, username, password)
        self.assertTrue(self.login.is_valid(username, password))

    def testValidateWrong(self):
        # Test 8 checks that the login can detect an incorrect admin login
        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"
        self.login.add_user(id, first_name, last_name, username, password)
        self.assertFalse(self.login.is_valid(username, "Wrong Password"))

    def testCasingForUsername(self):
        # Test 9 Usernames should not be case-sensitive for loging in
        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)
        self.assertTrue(self.login.is_valid(username.upper(), password))

    def testCasingForIsUnique(self):
        # Test 10 Casing should not matter when checking if it is unique
        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)
        self.assertFalse(self.login.is_username_unique(username.upper()))

    def testExistUsername(self):
        # Test 11 This test validates the function isUsernameExist
        # which will return true is the username does not
        # already exist in the database
        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)
        self.assertFalse(self.login.is_username_unique(username))
        self.assertTrue(self.login.is_username_unique(username + "33"))

    def testDuplicateUsername(self):
        # Test 12 This test ensures an error is thrown if an attempt to insert an already existing username into the
        # table
        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)

        with self.assertRaises(login.DatabaseError) as db_error:
            self.login.add_user(id, first_name, last_name, username, password)

        exception = db_error.exception
        self.assertEqual(exception.message, f"Could not add {username} to table -> UNIQUE constraint failed: "
                                            f"user.user_id")

    def testFindFirstName(self):
        # Test 13 get user should return the correct first name

        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)
        self.assertEqual("Bat", self.login.get_user(username)[0][0])

    def testFindLastName(self):
        # Test 13 get user should return the correct last name

        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)
        self.assertEqual("Man", self.login.get_user(username)[0][1])

    def testFindUsername(self):
        # Test 13 get user should return the correct username

        id = 3
        first_name = "Bat"
        last_name = "Man"
        password = "ghru222"
        username = "batman333"

        self.login.add_user(id, first_name, last_name, username, password)
        self.assertEqual("batman333", self.login.get_user(username)[0][2])


if __name__ == '__main__':
    unittest.main()
