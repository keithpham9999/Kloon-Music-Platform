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
            genre        VARCHAR(16) NOT NULL,
            source         VARCHAR(16) NOT NULL
            )''')

        self.execute(
            '''CREATE TABLE IF NOT EXISTS genre(
            genre_id  INT PRIMARY KEY,
            genre_name      VARCHAR(16) NOT NULL
            )''')

        self.commit()

    def fill_genre(self):
        """Fills the genre table with the different categories for a meal
        """
        # These inserts the only valid options for an item type
        try:
            self.execute("INSERT INTO genre "
                         "values(1, 'House')")
            self.execute("INSERT INTO genre "
                         "values(2, 'Hardstyle')")
            self.execute("INSERT INTO genre "
                         "values(3, 'Trap')")
            self.execute("INSERT INTO genre "
                         "values(4, 'Drum&Bass')")
            self.commit()
        except:
            pass

    def fill_music(self):
        """Fills the music table with the tracks
        """
        # This method was required for testing against a database, it will be removed once there is a database
        # set in place
        try:
            self.execute("INSERT INTO music values(1, '4B x Junkie Kid - Love Is Dead.mp3','Love Is Dead',"
                         "'4B, Junkie K', 'Hardstyle','music/4B x Junkie Kid - Love Is Dead.mp3')")
            self.execute("INSERT INTO music values(2, 'Brooks - Lynx.mp3','Lynx',"
                         "'Brooks', 'House','music/Brooks - Lynx.mp3')")
            self.execute("INSERT INTO music values(3, 'Calvin Harris & Disciples - How Deep Is Your Love.mp3',"
                         "'How Deep Is Your Love',"
                         "'Calvin Harris & Disciples', 'House',"
                         "'music/Calvin Harris & Disciples - How Deep Is Your Love.mp3')")
            self.execute("INSERT INTO music values(4, 'David Guetta & Showtek - Your Love.mp3','Your Love',"
                         "'David Guetta & Showtek', 'House','music/David Guetta & Showtek - Your Love.mp3')")
            self.execute("INSERT INTO music values(5, 'Grafix - Radiance.mp3','Radiance',"
                         "'Grafix', 'Drum&Bass','music/Grafix - Radiance.mp3')")
            self.execute("INSERT INTO music values(6, 'Higher Brothers & DJ Snake - Made In China.mp3',"
                         "'Made In China',"
                         "'4Higher Brothers & DJ Snake', 'Trap',"
                         "'music/Higher Brothers & DJ Snake - Made In China.mp3')")
            self.execute("INSERT INTO music values(7, 'James Hype, Miggy Dela Rosa - Ferrari.mp3',"
                         "'Ferrari',"
                         "'James Hype, Miggy Dela Rosa', "
                         "'House','music/James Hype, Miggy Dela Rosa - Ferrari.mp3')")
            self.execute("INSERT INTO music values(8, 'Knock2 - Dashstar.mp3',"
                         "'Dashstar',"
                         "'Knock2', 'House','music/Knock2 - Dashstar.mp3')")
            self.execute("INSERT INTO music values(9, 'LOOPERS, Seth Hills - Out Of Control.mp3',"
                         "'Out Of Control',"
                         "'LOOPERS, Seth Hills', 'House','music/LOOPERS, Seth Hills - Out Of Control.mp3')")
            self.execute("INSERT INTO music values(10, 'Martin Garrix & Mesto - Limitless.mp3',"
                         "'Limitless',"
                         "'Martin Garrix & Mesto', 'House','music/Martin Garrix & Mesto - Limitless.mp3')")
            self.execute("INSERT INTO music values(11, 'Martin Garrix & Zedd - Follow.mp3',"
                         "'Follow',"
                         "'Martin Garrix & Zedd', 'House','music/Martin Garrix & Zedd - Follow.mp3')")
            self.execute("INSERT INTO music values(12, 'Oliver Tree & Robin Schulz - Miss You.mp3',"
                         "'Miss You',"
                         "'Oliver Tree & Robin Schulz', 'House','music/Oliver Tree & Robin Schulz - Miss You.mp3')")
            self.execute("INSERT INTO music values(13, 'Sam Smith, Kim Petras - Unholy (ACRAZE Remix).mp3',"
                         "'Unholy (ACRAZE Remix)',"
                         "'Sam Smith, Kim Petras', 'House','music/Sam Smith, Kim Petras - Unholy (ACRAZE Remix).mp3')")
            self.execute("INSERT INTO music values(14, 'SMACK x Raven & Kreyn - Boom Boom (feat. CHYL).mp3',"
                         "'Boom Boom (feat. CHYL)',"
                         "'SMACK x Raven & Kreyn', 'House','music/SMACK x Raven & Kreyn - Boom Boom (feat. CHYL).mp3')")
            self.execute("INSERT INTO music values(15, 'Sub Focus & Dimension - Desire.mp3',"
                         "'Desire',"
                         "'Sub Focus & Dimension', 'Drum&Bass','music/Sub Focus & Dimension - Desire.mp3')")
            self.execute("INSERT INTO music values(16, 'Touliver X SlimV - Em Oi Cu Vui.mp3',"
                         "'Em Oi Cu Vui',"
                         "'Touliver X SlimV', 'House','music/Touliver X SlimV - Em Oi Cu Vui.mp3')")
            self.execute("INSERT INTO music values(17, 'Valentino Khan - Deep Down Low.mp3',"
                         "'Deep Down Low',"
                         "'Valentino Khan', 'House','music/Valentino Khan - Deep Down Low.mp3')")
            self.execute("INSERT INTO music values(18, 'W&W & Blasterjaxx - Bowser.mp3',"
                         "'Bowser',"
                         "'W&W & Blasterjaxx', 'House','music/W&W & Blasterjaxx - Bowser.mp3')")
            self.execute("INSERT INTO music values(19, 'Öwnboss, Sevek - Move Your Body.mp3',"
                         "'Move Your Body',"
                         "'Öwnboss, Sevek', 'House','music/Öwnboss, Sevek - Move Your Body.mp3')")
            self.execute("INSERT INTO music values(20, 'Andromedik & Luka - Lied To You.mp3',"
                         "'Lied To You',"
                         "'Andromedik & Luka', 'Drum&Bass','music/Andromedik & Luka - Lied To You.mp3')")
            self.execute("INSERT INTO music values(21, 'Artificial Intelligence - Eastern Surprise.mp3',"
                         "'Eastern Surprise',"
                         "'Artificial Intelligence', 'Drum&Bass',"
                         "'music/Artificial Intelligence - Eastern Surprise.mp3')")
            self.execute("INSERT INTO music values(22, 'Bastion - Skin (ft. Zara Kershaw).mp3',"
                         "'Skin',"
                         "'Bastion', 'Drum&Bass','music/Bastion - Skin (ft. Zara Kershaw).mp3')")
            self.execute("INSERT INTO music values(23, 'BCee, Charlotte Haining & Emba - Before You.mp3',"
                         "'Before You',"
                         "'BCee, Charlotte Haining & Emba', 'Drum&Bass',"
                         "'music/BCee, Charlotte Haining & Emba - Before You.mp3')")
            self.execute("INSERT INTO music values(24, 'BCee, Charlotte Haining & Emba - "
                         "Before You (goddard. Remix).mp3',"
                         "'Before You (goddard. Remix)',"
                         "'BCee, Charlotte Haining & Emba', 'Drum&Bass',"
                         "'music/BCee, Charlotte Haining & Emba - Before You (goddard. Remix).mp3')")
            self.execute("INSERT INTO music values(25, 'BCee, L Side & Charlotte Haining - Crossroad.mp3',"
                         "'Crossroad',"
                         "'BCee, L Side & Charlotte Haining', 'Drum&Bass',"
                         "'music/BCee, L Side & Charlotte Haining - Crossroad.mp3')")
            self.execute("INSERT INTO music values(26, 'BCee & Charlotte Haining - Is It Real.mp3',"
                         "'Is It Real',"
                         "'BCee & Charlotte Haining', 'Drum&Bass','music/BCee & Charlotte Haining - Is It Real.mp3')")
            self.execute("INSERT INTO music values(27, 'BCee & T.R.A.C - Picture Disc.mp3',"
                         "'Picture Disc',"
                         "'BCee & T.R.A.C', 'Drum&Bass','music/BCee & T.R.A.C - Picture Disc.mp3')")
            self.execute("INSERT INTO music values(28, 'Boxplot - Only Us.mp3',"
                         "'Only Us',"
                         "'Boxplot', 'Drum&Bass','music/Boxplot - Only Us.mp3')")
            self.execute("INSERT INTO music values(29, 'Boxplot - We Lose It All (ft. Voicians).mp3',"
                         "'We Lose It All (ft. Voicians)',"
                         "'Boxplot', 'Drum&Bass','music/Boxplot - We Lose It All (ft. Voicians).mp3')")
            self.execute("INSERT INTO music values(30, 'CamelPhat ft. LOWES - Easier (Sub Focus Remix).mp3',"
                         "'Easier (Sub Focus Remix)',"
                         "'CamelPhat ft. LOWES', 'Drum&Bass',"
                         "'music/CamelPhat ft. LOWES - Easier (Sub Focus Remix).mp3')")
            self.execute("INSERT INTO music values(31, 'Capturelight - Lonesome.mp3',"
                         "'Lonesome',"
                         "'Capturelight', 'Drum&Bass','music/Capturelight - Lonesome.mp3')")
            self.execute("INSERT INTO music values(32, 'Charli Brix - MAZI (Ft. Lenzman & Slay).mp3',"
                         "'MAZI (Ft. Lenzman & Slay)',"
                         "'Charli Brix', 'Drum&Bass','music/Charli Brix - MAZI (Ft. Lenzman & Slay).mp3')")
            self.execute("INSERT INTO music values(33, 'D-Code & Psylence - Coming Down (ft. Jessica Wilde).mp3',"
                         "'Coming Down (ft. Jessica Wilde)',"
                         "'SD-Code & Psylence', 'Drum&Bass',"
                         "'music/D-Code & Psylence - Coming Down (ft. Jessica Wilde).mp3')")
            self.execute("INSERT INTO music values(34, 'Dawn Wall - Judgement.mp3',"
                         "'Judgement',"
                         "'Dawn Wall', 'Drum&Bass','music/Dawn Wall - Judgement.mp3')")
            self.execute("INSERT INTO music values(35, 'Dawn Wall - Movies.mp3',"
                         "'Movies',"
                         "'Dawn Wall', 'Drum&Bass','music/Dawn Wall - Movies.mp3')")
            self.execute("INSERT INTO music values(36, 'Delta Heavy - No Gravity.mp3',"
                         "'No Gravity',"
                         "'Delta Heavy', 'Drum&Bass','music/Delta Heavy - No Gravity.mp3')")
            self.execute("INSERT INTO music values(37, 'Droeloe x Imanu - Catalyst.mp3',"
                         "'Catalyst',"
                         "'Droeloe x Imanu', 'Drum&Bass','music/Droeloe x Imanu - Catalyst.mp3')")
            self.execute("INSERT INTO music values(38, 'Dub Phizix - City of Glass.mp3',"
                         "'City of Glass',"
                         "'Dub Phizix', 'Drum&Bass','music/Dub Phizix - City of Glass.mp3')")
            self.execute("INSERT INTO music values(39, 'Elipsa - Addicted.mp3',"
                         "'Addicted',"
                         "'Elipsa', 'Drum&Bass','music/Elipsa - Addicted.mp3')")
            self.execute("INSERT INTO music values(40, 'Emz - Good Good (ft. Kanobie).mp3',"
                         "'Good Good (ft. Kanobie)',"
                         "'Emz', 'Drum&Bass','music/Emz - Good Good (ft. Kanobie).mp3')")
            self.execute("INSERT INTO music values(41, 'Feint - We Wont Be Alone (feat. Laura Brehm).mp3',"
                         "'We Wont Be Alone (feat. Laura Brehm)',"
                         "'Feint', 'Drum&Bass','music/Feint - We Wont Be Alone (feat. Laura Brehm).mp3')")
            self.execute("INSERT INTO music values(42, 'Fred V & Grafix - Ultraviolet.mp3',"
                         "'Ultraviolet',"
                         "'Fred V & Grafix', 'Drum&Bass','music/Fred V & Grafix - Ultraviolet.mp3')")
            self.execute("INSERT INTO music values(43, 'goddard. & Charlotte Haining - Feel Like That.mp3',"
                         "'Feel Like That',"
                         "'goddard. & Charlotte Haining', 'Drum&Bass',"
                         "'music/goddard. & Charlotte Haining - Feel Like That.mp3')")
            self.execute("INSERT INTO music values(44, 'Grafix - Alone (ft. Ruth Royall).mp3',"
                         "'Alone (ft. Ruth Royall)',"
                         "'Grafix', 'Drum&Bass','music/Grafix - Alone (ft. Ruth Royall).mp3')")
            self.execute("INSERT INTO music values(45, 'Grafix - Onyx (feat. Chrissie Huntley).mp3',"
                         "'Onyx (feat. Chrissie Huntley)',"
                         "'Grafix', 'Drum&Bass','music/Grafix - Onyx (feat. Chrissie Huntley).mp3')")
            self.execute("INSERT INTO music values(46, 'Grafix - Refuge (ft. Ruth Royall).mp3',"
                         "'Refuge (ft. Ruth Royall)',"
                         "'Grafix', 'Drum&Bass','music/Grafix - Refuge (ft. Ruth Royall).mp3')")
            self.execute("INSERT INTO music values(47, 'Grafix - Skyline (ft. Metrik).mp3',"
                         "'Skyline (ft. Metrik)',"
                         "'Grafix', 'Drum&Bass','music/Grafix - Skyline (ft. Metrik).mp3')")
            self.execute("INSERT INTO music values(48, 'Grafix - Somewhere (ft. Reiki Ruawai).mp3',"
                         "'Somewhere (ft. Reiki Ruawai)',"
                         "'Grafix', 'Drum&Bass','music/Grafix - Somewhere (ft. Reiki Ruawai).mp3')")
            self.execute("INSERT INTO music values(49, 'Grafix - Zephyr (feat. Ruth Royall).mp3',"
                         "'Zephyr (feat. Ruth Royall)',"
                         "'SMACK x Raven & Kreyn', 'Drum&Bass','music/Grafix - Zephyr (feat. Ruth Royall).mp3')")
            self.execute("INSERT INTO music values(50, 'Halogenix - Lost Friends.mp3',"
                         "'Lost Friends',"
                         "'Halogenix', 'Drum&Bass','music/Halogenix - Lost Friends.mp3')")
            self.execute("INSERT INTO music values(51, 'Hiraeth & TZ - If We Wait (ft. Siege MC).mp3',"
                         "'If We Wait (ft. Siege MC)',"
                         "'Hiraeth & TZ', 'Drum&Bass','music/Hiraeth & TZ - If We Wait (ft. Siege MC).mp3')")
            self.execute("INSERT INTO music values(52, 'Hybrid Minds & Birdy - State Lines.mp3',"
                         "'State Lines',"
                         "'Hybrid Minds & Birdy', 'Drum&Bass','music/Hybrid Minds & Birdy - State Lines.mp3')")
            self.execute("INSERT INTO music values(53, 'Hybrid Minds & Grace Grundy - Fingerprints.mp3',"
                         "'Fingerprints',"
                         "'Hybrid Minds & Grace Grundy', 'Drum&Bass',"
                         "'music/Hybrid Minds & Grace Grundy - Fingerprints.mp3')")
            self.execute("INSERT INTO music values(54, 'Hybrid Minds & Tom Cane - Not Alone.mp3',"
                         "'Not Alone',"
                         "'Hybrid Minds & Tom Cane', 'Drum&Bass','music/Hybrid Minds & Tom Cane - Not Alone.mp3')")
            self.execute("INSERT INTO music values(55, 'Hybrid Minds & Tom Walker - Castles.mp3',"
                         "'Castles',"
                         "'Hybrid Minds & Tom Walker', 'Drum&Bass','music/Hybrid Minds & Tom Walker - Castles.mp3')")
            self.execute("INSERT INTO music values(56, 'Hybrid Minds - Touch (ft. Tiffani Juno).mp3',"
                         "'Touch (ft. Tiffani Juno)',"
                         "'Hybrid Minds', 'Drum&Bass','music/Hybrid Minds - Touch (ft. Tiffani Juno).mp3')")
            self.execute("INSERT INTO music values(57, 'Leniz - Mourning Tears.mp3',"
                         "'Mourning Tears',"
                         "'Leniz', 'Drum&Bass','music/Leniz - Mourning Tears.mp3')")
            self.execute("INSERT INTO music values(58, 'Maduk - Colours (ft. Diamond Eyes).mp3',"
                         "'Colours (ft. Diamond Eyes)',"
                         "'Maduk', 'Drum&Bass','music/Maduk - Colours (ft. Diamond Eyes).mp3')")
            self.execute("INSERT INTO music values(59, 'Metrik & Grafix - Overdrive.mp3',"
                         "'Overdrive',"
                         "'Metrik & Grafix', 'Drum&Bass','music/Metrik & Grafix - Overdrive.mp3')")
            self.execute("INSERT INTO music values(60, 'Metrik - Automata.mp3',"
                         "'Automata',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Automata.mp3')")
            self.execute("INSERT INTO music values(61, 'Metrik - Gravity.mp3',"
                         "'Gravity',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Gravity.mp3')")
            self.execute("INSERT INTO music values(62, 'Metrik - Hackers.mp3',"
                         "'Hackers',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Hackers.mp3')")
            self.execute("INSERT INTO music values(63, 'Metrik - Immortal.mp3',"
                         "'Immortal',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Immortal.mp3')")
            self.execute("INSERT INTO music values(64, 'Metrik - Parallel (ft. Grafix).mp3',"
                         "'Parallel (ft. Grafix)',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Parallel (ft. Grafix).mp3')")
            self.execute("INSERT INTO music values(65, 'Metrik - Time To Let Go.mp3',"
                         "'Time To Let Go',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Time To Let Go.mp3')")
            self.execute("INSERT INTO music values(66, 'Metrik - Utopia.mp3',"
                         "'Utopia',"
                         "'Metrik', 'Drum&Bass','music/Metrik - Utopia.mp3')")
            self.execute("INSERT INTO music values(67, 'Millbrook - Inspire (ft. BRAVVN).mp3',"
                         "'Inspire (ft. BRAVVN)',"
                         "'Millbrook', 'Drum&Bass','music/Millbrook - Inspire (ft. BRAVVN).mp3')")
            self.execute("INSERT INTO music values(68, 'Mitekiss - Love Me, Haunt Me.mp3',"
                         "'Love Me, Haunt Me',"
                         "'Mitekiss', 'Drum&Bass','music/Mitekiss - Love Me, Haunt Me.mp3')")
            self.execute("INSERT INTO music values(69, 'Monrroe & Duskee - Reluctant (ft. Nina Arya).mp3',"
                         "'Reluctant (ft. Nina Arya)',"
                         "'Monrroe & Duskee', 'Drum&Bass','music/Monrroe & Duskee - Reluctant (ft. Nina Arya).mp3')")
            self.execute("INSERT INTO music values(70, 'Particle & En_vy - With U.mp3',"
                         "'With U',"
                         "'Particle & En_vy', 'Drum&Bass','music/Particle & En_vy - With U.mp3')")
            self.execute("INSERT INTO music values(71, 'Polaris & Schematic & Natalie Wood - Inner Vision.mp3',"
                         "'Inner Vision',"
                         "'Polaris & Schematic & Natalie Wood', 'Drum&Bass',"
                         "'music/Polaris & Schematic & Natalie Wood - Inner Vision.mp3')")
            self.execute("INSERT INTO music values(72, 'pyxis & IYRE - Traverse.mp3',"
                         "'Traverse',"
                         "'pyxis & IYRE', 'Drum&Bass','music/pyxis & IYRE - Traverse.mp3')")
            self.execute("INSERT INTO music values(73, 'pyxis & Kleu - Solaris.mp3',"
                         "'Solaris',"
                         "'pyxis & Kleu', 'Drum&Bass','music/pyxis & Kleu - Solaris.mp3')")
            self.execute("INSERT INTO music values(74, 'Radiax - Headway.mp3',"
                         "'Headway',"
                         "'Radiax', 'Drum&Bass','music/Radiax - Headway.mp3')")
            self.execute("INSERT INTO music values(75, 'Satl - Karma (ft. Frank H. Carter III).mp3',"
                         "'Karma (ft. Frank H. Carter III)',"
                         "'Satl', 'Drum&Bass','music/Satl - Karma (ft. Frank H. Carter III).mp3')")
            self.execute("INSERT INTO music values(76, 'skantia - Autumn Leaves.mp3',"
                         "'Autumn Leaves',"
                         "'skantia', 'Drum&Bass','music/skantia - Autumn Leaves.mp3')")
            self.execute("INSERT INTO music values(77, 'Skylark & GROUND - Cobalt.mp3',"
                         "'Cobalt',"
                         "'Skylark & GROUND', 'Drum&Bass','music/Skylark & GROUND - Cobalt.mp3')")
            self.execute("INSERT INTO music values(78, 'SOLAH - King.mp3',"
                         "'King',"
                         "'SOLAH', 'Drum&Bass','music/SOLAH - King.mp3')")
            self.execute("INSERT INTO music values(79, 'SOLAH - Tempo.mp3',"
                         "'Tempo',"
                         "'SOLAH', 'Drum&Bass','music/SOLAH - Tempo.mp3')")
            self.execute("INSERT INTO music values(80, 'SOLAH - Time.mp3',"
                         "'Time',"
                         "'SOLAH', 'Drum&Bass','music/SOLAH - Time.mp3')")
            self.execute("INSERT INTO music values(81, 'Sub Focus - Vibration (One More Time) ft. ARCO.mp3',"
                         "'Vibration (One More Time) ft. ARCO',"
                         "'Sub Focus', 'Drum&Bass','music/Sub Focus - Vibration (One More Time) ft. ARCO.mp3')")
            self.execute("INSERT INTO music values(82, 'Sub_liminal & Nelver - Free Your Mind (ft. Gemma Rose).mp3',"
                         "'Free Your Mind (ft. Gemma Rose)',"
                         "'Sub_liminal & Nelver', 'Drum&Bass',"
                         "'music/Sub_liminal & Nelver - Free Your Mind (ft. Gemma Rose).mp3')")
            self.execute("INSERT INTO music values(83, 'Sub_liminal & Resurgence - Mind Shadows.mp3',"
                         "'Mind Shadows',"
                         "'Sub_liminal & Resurgence', 'Drum&Bass','music/Sub_liminal & Resurgence - Mind Shadows.mp3')")
            self.execute("INSERT INTO music values(84, 'Supercurve - Frequency.mp3',"
                         "'Frequency',"
                         "'Supercurve', 'Drum&Bass','music/Supercurve - Frequency.mp3')")
            self.execute("INSERT INTO music values(85, 'Synergy - All Makes Sense (ft. Tom Cane).mp3',"
                         "'All Makes Sense (ft. Tom Cane)',"
                         "'Synergy', 'Drum&Bass','music/Synergy - All Makes Sense (ft. Tom Cane).mp3')")
            self.execute("INSERT INTO music values(86, 'Talix - Say It.mp3',"
                         "'Say It',"
                         "'SMACK x Raven & Kreyn', 'Drum&Bass','music/Talix - Say It.mp3')")
            self.execute("INSERT INTO music values(87, 'Technimatic - Confide (ft. A Little Sound).mp3',"
                         "'Confide (ft. A Little Sound)',"
                         "'Technimatic', 'Drum&Bass','music/Technimatic - Confide (ft. A Little Sound).mp3')")
            self.execute("INSERT INTO music values(88, 'Telomic & Voicians - Night Echoes.mp3',"
                         "'Night Echoes',"
                         "'Telomic & Voicians', 'Drum&Bass','music/Telomic & Voicians - Night Echoes.mp3')")
            self.execute("INSERT INTO music values(89, 'The Caracal Project, Buunshin & Rhode - I Need A Break.mp3',"
                         "'I Need A Break',"
                         "'The Caracal Project, Buunshin & Rhode', 'Drum&Bass',"
                         "'music/The Caracal Project, Buunshin & Rhode - I Need A Break.mp3')")
            self.execute("INSERT INTO music values(90, 'The Vanguard Project - Stronger (ft. L.I.T.A).mp3',"
                         "'Stronger (ft. L.I.T.A)',"
                         "'The Vanguard Project', 'Drum&Bass',"
                         "'music/The Vanguard Project - Stronger (ft. L.I.T.A).mp3')")
            self.execute("INSERT INTO music values(91, 'Turno - Whats On Your Mind ft. SJ Loq (DNB Edit).mp3',"
                         "'Whats On Your Mind ft. SJ Loq (DNB Edit)',"
                         "'Turno', 'Drum&Bass','music/Turno - Whats On Your Mind ft. SJ Loq (DNB Edit).mp3')")
            self.execute("INSERT INTO music values(92, 'Vibe Chemistry - Rock To The Rhythm.mp3',"
                         "'Rock To The Rhythm',"
                         "'Vibe Chemistry', 'Drum&Bass','music/Vibe Chemistry - Rock To The Rhythm.mp3')")
            self.execute("INSERT INTO music values(93, 'Visages - Love Conspiration.mp3',"
                         "'Love Conspiration',"
                         "'Visages', 'Drum&Bass','music/Visages - Love Conspiration.mp3')")
            self.execute("INSERT INTO music values(94, 'Waeys - Set The Vibe (feat. flowanastasia).mp3',"
                         "'Set The Vibe (feat. flowanastasia)',"
                         "'Waeys', 'Drum&Bass','music/Waeys - Set The Vibe (feat. flowanastasia).mp3')")
            self.execute("INSERT INTO music values(95, 'Wilkinson & Becky Hill - Here For You.mp3',"
                         "'Here For You',"
                         "'Wilkinson & Becky Hill', 'Drum&Bass','music/Wilkinson & Becky Hill - Here For You.mp3')")
            self.execute("INSERT INTO music values(96, 'Wilkinson - Close Your Eyes (ft. Iiola).mp3',"
                         "'Close Your Eyes (ft. Iiola)',"
                         "'Wilkinson', 'Drum&Bass','music/Wilkinson - Close Your Eyes (ft. Iiola).mp3')")
            self.execute("INSERT INTO music values(97, 'Winslow - Thinking Of You (ft. T.R.A.C).mp3',"
                         "'Thinking Of You (ft. T.R.A.C)',"
                         "'Winslow ', 'Drum&Bass','music/Winslow - Thinking Of You (ft. T.R.A.C).mp3')")
            self.execute("INSERT INTO music values(98, 'Workforce - Forever.mp3',"
                         "'Forever',"
                         "'Workforce', 'Drum&Bass','music/Workforce - Forever.mp3')")
            self.execute("INSERT INTO music values(99, 'Xeonz - Perfectly Splendid.mp3',"
                         "'Perfectly Splendid',"
                         "'Xeonz', 'Drum&Bass','music/Xeonz - Perfectly Splendid.mp3')")
            self.execute("INSERT INTO music values(100, 'Lenzman & Redeyes - Wet Like Water.mp3',"
                         "'Wet Like Water',"
                         "'Lenzman & Redeyes', 'Drum&Bass','music/Lenzman & Redeyes - Wet Like Water.mp3')")




            self.commit()
        except sqlite3.IntegrityError:
            pass


    def music_reset(self):
        """Resets the music table
        """
        self.execute("DROP table IF EXISTS music")
        self.execute("DROP table IF EXISTS genre")
        self.commit()
        self.create_music_tables()
        self.fill_music()
        self.fill_genre()

    def close(self):
        """Terminates the connection to the database
        """
        self.conn.close()
