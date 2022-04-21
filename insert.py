from unittest import main
from pyArango.connection import *

if __name__ == '__main__':
    #Conectar
    conn = Connection(arangoURL = "http://localhost:8529", username="root", password="root")
    db = conn['MUSICAS']
    collection = db['Music']
    #Inserir dados
    musicas = [
        ('HUMBLE', 'Kendrick Lamar', '2017'), 
        ('DNA', 'Kendrick Lamar', '2017'),
        ('False Need', 'Mochakk', '2022'),
        ('Again', 'Victor Lou', '2021')
    ]
    for (nome, artista, ano) in musicas:
            documento = collection.createDocument()
            documento['nome'] = nome
            documento['artista'] = artista
            documento['ano'] = ano
            documento._key = nome.replace(" ", "").lower()
            documento.save()
  