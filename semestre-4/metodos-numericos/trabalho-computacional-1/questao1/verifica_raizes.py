def verifica_raizes(raizes, coeficientes):
    for indice, raiz in enumerate(raizes):
        fx = 0
        for index, coeficiente in enumerate(coeficientes):
            fx += coeficiente * (raiz ** (len(coeficientes) - 1))
        print("Valor do fx{} = {:3f}".format(indice+1, fx))
