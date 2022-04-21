#Cria uma coleção chamada "Music", no banco de dados "MUSICA" criado previamente no ArangoDB.

from pyArango.connection import *

if __name__ == '__main__':
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    db = conn['MUSICAS']
    db.createCollection(name='Music')