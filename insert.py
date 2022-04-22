#Insere documentos na coleção.

from unittest import main
from pyArango.connection import *

if __name__ == '__main__':
    #Conexão
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    #Acesso ao banco de dados
    db = conn['musicas']
   
    #Inserir dados
    musicas = [
        ('HUMBLE', 'Kendrick Lamar', '2017'), 
        ('DNA', 'Kendrick Lamar', '2017'),
        ('False Need', 'Mochakk', '2022'),
        ('Again', 'Victor Lou', '2021'),
        ('Enter Sandman', 'Metallica', '1991'),
        ('Sad But True', 'Metallica', '1991')
    ]
    for (nome, artista, ano) in musicas:
            key = "_".join([nome.replace(" ", "").lower(),artista.replace(" ", "").lower()])
            doc = {'_key': key, 'nome': nome, 'artista': artista, 'ano': ano}
            bind = {"doc": doc}
            query = """INSERT @doc INTO Music"""
            db.AQLQuery(query, bindVars=bind)
  