from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

xpos = 200
ypos = 200
width = 300
height = 300

class Song:
    artist = ''
    title = ''

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def display_cover_art(self):
        # pixmap shows the picture
        # b2.setIcon(QIcon(QPixmap("python.gif")))
        pass

    def display_song_title(self):
        pass

def like_listener(self):
    # adds song to a "likes list"
    # advances onto the next song
    print("Clicked like button")

def dislike_listener(self):
    print("Clicked dislike button")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("Spotify 4 Qts")
        self.initUI()
    def initUI(self):
        # Dislike Button
        self.dislike_button = QtWidgets.QPushButton(self)
        self.dislike_button.setText("Dislike")
        self.dislike_button.clicked.connect(dislike_listener)
        self.dislike_button.move(0, height/2 - 10)

        # Like Button
        self.like_button = QtWidgets.QPushButton(self)
        self.like_button.setText("Like")
        self.like_button.clicked.connect(like_listener)
        self.like_button.move(200, height/2 - 10)

        # Cover art Placeholder?
        
        # self.dog = QtWidgets.QPushButton(self.centralwidget)
        # self.dog.setGeometry(QtCore.QRect(410, 510, 391, 41))
        # self.dog.setObjectName("dog")

def window():
    # knows which OS to display
    app = QApplication(sys.argv)
    win = MyWindow()
    # x,y to show on screen, width&height 
    win.setGeometry(xpos, ypos, width, height)
    win.setWindowTitle("Spotify 4 Qts")

    win.show()
    # start the app
    sys.exit(app.exec_())

    # 1. cover art
    # 2. media player
    # 3. dislike
    # 4. like

window()