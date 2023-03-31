import unittest

import src.main.python.Database as database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = database.Database()
        self.database.music_reset()
        self.database.fill_genre()
        self.database.fill_music()


if __name__ == '__main__':
    unittest.main()
