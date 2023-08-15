class Song:
    count = 0
    genres = []
    genre_count = {}
    artists = []
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)
        self.add_to_genre_count(self.genre)
        self.add_to_genres()
        self.add_to_artist_count(self.artist)
        
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1


    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))

    
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count.keys():
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1


    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))


    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count.keys():
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
