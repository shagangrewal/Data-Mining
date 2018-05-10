import webbrowser

class Movie():
    def __init__(self,name,story,pic,video):
        self.title = name
        self.storyline = story
        self.poster = pic
        self.trailer = video

    def show_trailer(self):
        webbrowser.open(self.trailer)
