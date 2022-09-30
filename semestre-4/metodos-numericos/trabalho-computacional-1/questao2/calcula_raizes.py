import numpy as np


def calcula_raizes(inicio, fim, funcao,  metodo, fragmentador=1000):
    intervalos = encontrarIntervalosProvaveis(
        inicio, fim, funcao, fragmentador)
    print("Lista de intervalos = ", intervalos)
    return chama_metodo(intervalos, funcao, metodo)


def encontrarIntervalosProvaveis(inicio, fim, funcao, fragmentador):
    candidatos = np.linspace(inicio, fim, fragmentador)

    possiveisZeros = []
    tamanho = len(candidatos)
    intervalo = (inicio - fim)/fragmentador

    for index, elementos in enumerate(candidatos):
        if (funcao(elementos) * funcao(elementos + intervalo) < 0):
            possiveisZeros.append([elementos, elementos + intervalo])
        if (index == tamanho):
            continue
    return possiveisZeros


def chama_metodo(listaIntervalos, funcao, metodo):
    raizes = []

    for menor, maior in listaIntervalos:
        raizes.append(metodo(menor, maior, funcao))

    return raizes
