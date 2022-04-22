#Carrega os documentos de acordo com o artista indicado.

from pyArango.connection import *

if __name__ == '__main__':
    print("\n------------------------------------------\n")
    
    #Conexão
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    #Acesso ao banco de dados
    db = conn['musicas']

    query = """FOR documento IN Music FILTER documento.artista == 'Metallica' RETURN documento"""
    queryResult = db.AQLQuery(query, rawResults=True, batchSize=100)
    
    for documento in queryResult:
        print("[ Chave: %s ]" % documento['_key'])
        # document = collection[key]
        print("\n> Nome da música: %s\n> Artista: %s\n> Ano: %s\n" % (documento['nome'], documento['artista'], documento['ano']))

        print("------------------------------------------\n")