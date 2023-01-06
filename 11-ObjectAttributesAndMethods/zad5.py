class MusicPiece:
    def __init__(self, artist, trackTitle, album, year):
        self.artist = artist
        self.trackTitle = trackTitle
        self.album = album
        self.year = year

    def __str__(self):
        return "{:<10} {:<10}\n{:<10} {:<10}\n{:<10} {:<10}\n{:<10} {:<10}\n\n".format('Performer:', self.artist, 'Song:', self.trackTitle, 'Album:', self.album, 'Year:', self.year)


print(MusicPiece('Ed Sheeran', "Hearts Don't Break Around Here", 'Divide', '2017'))
print(MusicPiece('Performer1', 'Song1', 'Album1', '2222'))
print(MusicPiece('Performer2', 'Song2', 'Album2', '2337'))
