import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist_repository.delete_all()
album_repository.delete_all()

artist_1 = Artist ('Prince')
artist_repository.save(artist)

album = Album('Purple Rain', 'Movie Soundtrack', 'Prince')
album_repository.save(album)




pdb.set_trace()
