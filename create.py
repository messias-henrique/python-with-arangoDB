#Cria um banco de dados com nome de "musica" no servidor do ArangoDB.
#Cria uma coleção chamada "Music", dentro do banco de dados "musica".

from pyArango.connection import *

if __name__ == '__main__':
    #Conexão
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    
    #Criar o banco de dados
    db = conn.createDatabase(name="musicas")
    
    #Criar a coleção
    db = conn['musicas']
    db.createCollection(name='Music')