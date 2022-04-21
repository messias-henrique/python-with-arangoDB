#Faz a alteração de um campo do documento com a chave informada.

from pyArango.connection import *

if __name__ == '__main__':
    
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    db = conn['MUSICAS']
    collection = db['Music']
   
    document = collection['again']
    
    document['artista'] = "Roberto Carlos"
    document.save()