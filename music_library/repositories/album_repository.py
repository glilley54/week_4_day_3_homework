from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO album (title ,genre, artist, id) VALUES (%s,%s %s,%s) RETURNING*"
    values = [album.title,album.genre,album.artist,album.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    return album

def delete_all():
    pass


def select(id):
    pass


def delete(id):
    pass
