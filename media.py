import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, title, poster_image, trailer):
        self.title = title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """ Show the movie trailer """
        webbrowser.open(self.trailer_youtube_url)