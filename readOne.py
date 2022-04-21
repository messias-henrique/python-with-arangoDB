#Carrega o documento que possui a chave "falseneed" e mostra os campos na tela.

from pyArango.connection import *

if __name__ == '__main__':

    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    db = conn['MUSICAS']
    collection = db['Music']
    
    document = collection['falseneed']
    
    print("\nNome da música: %s\nArtista: %s\nAno: %s\n" % (document['nome'], document['artista'], document['ano']))