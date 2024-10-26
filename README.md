# Final Year Project

This is my Final Year Project

It is a web application named Kloon. Kloon is a music streaming platform that is open and free to all of the users. Music can all be streamed onine with no restrictions or premium plan to unlock new features. With my deep passion for Drum and Bass music, I will focus entirely on making this music platform just for Drum and Bass music so it will become a Drum and Bass community for Drum and Bass listener. 

From here, Drum and Bass head will be exposed to the music of their likings as Drum and Bass starts to evolve more and more day by day.

It is made with the inspiration from Spotify. In here I will try to create a user-friendly interface for users with some extensions of the functionalities apart from just user login.

Overall, I am thinking of the new theme layout for my project and any features to make my project unique and disctinct from Spotify. However, the innitial idead was based on Spotify so it will carry some inherited features or logic in my project.


EDIT CONFIGURATION FOR MAIN KLOON APPLICATION IN PYCHARM

When configuring the project in Pycharm IDE, make sure that the script path is:

/Users/user/PROJECT/src/main/python/Kloon.py

to be able to run the entire application.

Evironment variable should be: 
PYTHONUNBUFFERED=1

Python version should just be compatible with your most updated Python version on your local machine:
For me it is Pyton 3.10

MAKE SURE the working directory is always cut down and limited to just:

/Users/user/PROJECT

with no other further sub-directories

EDIT CONFIGURATION FOR UNIT TESTS IN PYCHARM:

Always make the target as the script path. 

To make it less ambiguous we start with an example, the unit test script path for the Python file
MusicManager with the name of testMusicManager would be: 

/Users/user/PROJECT/src/test/python/testMusicManager.py

And of course, the working directory would still be:

/Users/user/PROJECT

without any further adjustments to it. We do all the same to the other test files. 

One more important step is that when testing with a specific python file, make sure that the 
import statements that have been commented out should be used and do vice versa for the original 
import statements. For example, instead of using these import statements: 

from Database import Database
from DatabaseError import DatabaseError

We can use this instead: 

from src.main.python.Database import Database
from src.main.python.DatabaseError import DatabaseError

By doing this, Pycharm will not complain about the not finding the source file and it will make life a lot easier.

Login credentials:

Username: oliver1999

Password: qwert123




