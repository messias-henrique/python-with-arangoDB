#Faz a alteração de um campo do documento com a chave informada.

from pyArango.connection import *

if __name__ == '__main__':
    
    #Conexão
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    
    #Acesso ao banco de dados.
    db = conn['musicas']
   
    key = 'again_victorlou'
    doc = {"artista": "Roberto Carlos"}
    bind = {"doc": doc, "key": key}
    query = """UPDATE @key WITH @doc IN Music"""
    db.AQLQuery(query, bindVars=bind)