import unittest

import src.main.python.MusicManager as music


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.music = music.MusicManager()
        self.music.music_reset()

    def testGenreID(self):
        # Test 1 make sure that genres are assigned to the right id
        id_1 = 1
        id_2 = 2
        id_3 = 3
        id_4 = 4
        self.assertEqual(id_1, self.music.get_genre()[0][0])
        self.assertEqual(id_2, self.music.get_genre()[1][0])
        self.assertEqual(id_3, self.music.get_genre()[2][0])
        self.assertEqual(id_4, self.music.get_genre()[3][0])

    def testGenreName(self):
        # Test 2 make sure that genres are assigned to the right name
        name_1 = "House"
        name_2 = "Hardstyle"
        name_3 = "Trap"
        name_4 = "Drum&Bass"
        self.assertEqual(name_1, self.music.get_genre()[0][1])
        self.assertEqual(name_2, self.music.get_genre()[1][1])
        self.assertEqual(name_3, self.music.get_genre()[2][1])
        self.assertEqual(name_4, self.music.get_genre()[3][1])

    def testTrackID(self):
        # Test 3 make sure that music has the right id
        id = 1
        self.assertEqual(id, self.music.get_music()[0][0])

    def testTrackSource(self):
        # Test 4 make sure that music has the right source
        source = "Grafix - Somewhere (ft. Reiki Ruawai).mp3"
        self.assertEqual(source, self.music.get_music()[47][1])

    def testTrackName(self):
        # Test 5 make sure that music has the right track name
        track_name = "Somewhere (ft. Reiki Ruawai)"
        self.assertEqual(track_name, self.music.get_music()[47][2])

    def testArtistName(self):
        # Test 6 make sure that music has the right artist name
        artist = "Grafix"
        self.assertEqual(artist, self.music.get_music()[47][3])

    def testTrackGenre(self):
        # Test 7 make sure that music has the right id
        genre = "Drum&Bass"
        self.assertEqual(genre, self.music.get_music()[47][4])

    def testTrackLocalSource(self):
        # Test 8 make sure that music has the right track local source
        local = "music/Grafix - Somewhere (ft. Reiki Ruawai).mp3"
        self.assertEqual(local, self.music.get_music()[47][5])


if __name__ == '__main__':
    unittest.main()
