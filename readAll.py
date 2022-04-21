from pyArango.connection import *

if __name__ == '__main__':
    

    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    db = conn['MUSICAS']
    collections = db['Music']
    for document in collections.fetchAll():
        print("\nNome da música: %s\nArtista: %s\nAno: %s\n" % (document['nome'], document['artista'], document['ano']))