import praw
import random
from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
import os
#shower thought app
windowHeight = 200
windowWidth = 500

app = QApplication([])


with open(r'stuf\actual projects\thought giver\important.txt', 'r') as f:
        file = f.read()
        redditinfo = eval(file)

reddit = praw.Reddit(username=redditinfo["username"],
                     password=redditinfo["password"],
                     client_id=redditinfo["client_id"],
                     client_secret=redditinfo["client_secret"],
                     user_agent=redditinfo["user_agent"]
)

subreddit_name = "Showerthoughts"
subreddit = reddit.subreddit(subreddit_name)

def getPost():
    posts = subreddit.top(limit=300)
    num = random.randint(0,300)
    for i,post in enumerate(posts):
        if i==num:
            title = post.title
            userid = post.id
            desc = post.selftext
            url = post.url
            upvotes = post.score
    return title, userid, desc, url, upvotes

class ThoughtWindow(QWidget):
    def __init__(self):
        super().__init__()

        title, userid, desc, url, upvotes = getPost()

        self.setWindowTitle(f"Shower Thought by {userid}")
        self.setFixedSize(QSize(windowWidth, windowHeight*2))
        self.mainlayout = QVBoxLayout()
        self.setStyleSheet("background-color : black")

        self.innerlayout = QHBoxLayout()

        post_title = QLabel(f"<h1> {title} </h1>")
        post_title.setWordWrap(True)
        post_title.setStyleSheet("color: #B87CFF")
        self.mainlayout.addWidget(post_title)

        post_desc = QLabel(desc)
        post_desc.setWordWrap(True)
        post_desc.setStyleSheet("color: #B87CFF")
        self.mainlayout.addWidget(post_desc)

        post_votes = QLabel(f"{upvotes} upvotes")
        post_votes.setWordWrap(True)
        post_votes.setStyleSheet("color: #B87CFF")
        self.innerlayout.addWidget(post_votes)

        post_url = QLabel()
        post_url.setText(f'<a href="{url}">Click to see post</a>')
        post_url.setOpenExternalLinks(True)
        self.innerlayout.addWidget(post_url)

        self.innerlayout.addWidget(QWidget())
        self.innerlayout.addWidget(QWidget())
        self.innerlayout.addWidget(QWidget())

        
        self.mainlayout.addLayout(self.innerlayout)
        self.setLayout(self.mainlayout)

        

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Shower Thoughts")
        self.setFixedSize(QSize(windowWidth, windowHeight))
        self.setStyleSheet("background-color:black")

        btn = QPushButton("Click for a thought", parent=self)
        btn.setStyleSheet("background-color : #B87CFF")
        btn.setFixedSize(200,50)
        btn.move(150,75)
        btn.clicked.connect(self.show_thought)

    def show_thought(self, checked):
        self.w = ThoughtWindow()
        self.w.show()

        



window = MainWindow()

window.show()
app.exec()





