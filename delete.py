#Exclui os documentos de acordo com o artista indicado.

from pyArango.connection import *

if __name__ == '__main__':
    #Conexão
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    #Acesso ao banco de dados
    db = conn['musicas']
    query = """FOR documento IN Music FILTER documento.artista == 'Metallica' REMOVE documento IN Music"""
    queryResult = db.AQLQuery(query)


    #Exclui tudo
    # query = """FOR documento IN Music REMOVE documento IN Music"""
    # queryResult = db.AQLQuery(query)