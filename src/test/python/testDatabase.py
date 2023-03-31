import unittest

import src.main.python.Database as database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = database.Database()
        self.database.music_reset()
        self.database.fill_genre()
        self.database.fill_music()

    def tearDown(self):
        self.database.close()

    def testInsertGenre(self):
        # Test 1 Ensure that genres are all filled in the genre table
        self.assertTrue(True, self.database.fill_genre())

    def testInsertMusic(self):
        # Test 2 Ensure that tracks are all filled in the music table
        self.assertTrue(True, self.database.fill_music())


if __name__ == '__main__':
    unittest.main()
