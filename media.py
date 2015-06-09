import webbrowser

# The base class of Movie
class Media():
  """ This provides a way to store media-related information """

  def __init__(self, title, description):
    self.title = title
    self.description = description


# Movie inherits from Media. This doesn't affect the
# application's functionality, but it was fun to get
# inheritance working!
class Movie(Media):
  """ This provides a way to store movie-related information """

  # This belongs to the class itself, since it's always
  # the same for every instance
  VALID_RATINGS = ["G", "PG", "PG-13", "R"]

  def __init__(self, title, description, poster_image, trailer_youtube):
    Media.__init__(self, title, description)
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
