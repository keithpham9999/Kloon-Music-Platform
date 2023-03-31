from flask import Flask, render_template
from flask import request

from Database import Database
from LogInManager import LogInManager
from MusicManager import MusicManager

# from src.main.python.Database import Database
# from src.main.python.LogInManager import LogInManager
# from src.main.python.MusicManager import MusicManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret key"


@app.route('/loginPage/')
def login_page_redirect():
    """Loads login page
    """
    return render_template('login.html')


@app.route('/musicPage/', methods=["POST", "GET"])
def music_page_redirect():
    """Loads music page
    """
    music_manager = MusicManager()
    tracks = music_manager.get_music()
    music_manager.close()

    return render_template('music_page.html', tracks=tracks)


@app.route('/', methods=['POST', 'GET'])
def index():
    """Renders the home page
    """

    music_manager = MusicManager()
    tracks = music_manager.get_music()
    music_manager.close()

    return render_template('home_page.html', tracks=tracks)


def add_music():
    """Adds music into database
    """
    music = Database()
    music.music_reset()
    music.close()


def add_user():
    """Add user into database
    """
    user = Database()
    login = LogInManager()
    user.user_reset()
    login.fill_user()
    user.close()
    login.close()


@app.route('/loginPage/', methods=['POST'])
def login():
    """Verifies a user once they have entered their login credentials
    """
    if request.method == "POST":
        login = LogInManager()
        username = request.form['username']
        password = request.form['password']
        is_in = login.is_valid(username, password)
        login.close()
        music_manager = MusicManager()
        tracks = music_manager.get_music()
        music_manager.close()

        if is_in:
            return render_template("music_page.html", tracks=tracks)

    return render_template("login.html", error=True)


if __name__ == "__main__":
    add_music()
    add_user()
    app.run(debug=True, port=6969)
