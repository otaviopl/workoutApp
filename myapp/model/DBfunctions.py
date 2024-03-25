from pymongo import MongoClient
from config import MONGODB_URL, DATABASE_NAME, COLLECTION_NAME


def makeDictBd(resultadoQuery):
    treinos_exercicios={}
    for resultado in resultadoQuery:
        nome_treino = resultado["name"]
        exercicios = [exercicio["weight"] for exercicio in resultado["Exercices"]]
        treinos_exercicios[nome_treino] = exercicios
    return treinos_exercicios

def makeConnectionBd():
    try:
        client= MongoClient(MONGODB_URL)
        db=client['wkapp']
        collection = db['workout']
    except:
        print('ERROR AT THE CONNECTION TO BD') 

def buscaResultadoBD(colecao):
    return colecao.find()
        
    