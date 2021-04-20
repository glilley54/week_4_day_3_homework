from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository

def save(artist):
    sql = "INSERT INTO artist(name, id) VALUES (%s,%s) RETURNING*"
    values = [artist.name,artist.id]
    results = run_sql(sql,values)
    id = results[0]['id']
    return artist

    

def delete_all():
    pass

def select(id):
    pass

def albums(artist):
    pass
