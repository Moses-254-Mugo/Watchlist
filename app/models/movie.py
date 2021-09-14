class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id #The movie id
        self.title = title # The name of the movie
        self.overview = overview # A short description on the movie
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster # The poster image for the movie
        self.vote_average = vote_average # Average rating of the movie
        self.vote_count = vote_count # How many people have rated the movie