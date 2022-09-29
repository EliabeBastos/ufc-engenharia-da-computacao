def metodo_bernoulli(vetor_coeficientes):
    variacoesFuncaoMaisX = encontrar_variacao_de_sinal(vetor_coeficientes)
    variacoesFuncaoMenosX = encontrar_variacao_de_sinal(
        funcao_menos_x(vetor_coeficientes))

    possibilidadesPositivas = encontrar_possiveis_quantidades_raizes(
        variacoesFuncaoMaisX)
    possibilidadesNegativas = encontrar_possiveis_quantidades_raizes(
        variacoesFuncaoMenosX)

    return criando_dicionario(possibilidadesNegativas, possibilidadesPositivas)


def encontrar_variacao_de_sinal(vetor_coeficientes):
    variacoes = 0
    for index, coeficiente in enumerate(vetor_coeficientes):
        if (index == 0):
            coeficienteAnterior = coeficiente
            continue
        if (coeficiente * coeficienteAnterior < 0):
            variacoes += 1
        coeficienteAnterior = coeficiente
    return variacoes


def encontrar_possiveis_quantidades_raizes(variacoes):
    possibilidades = []
    inteiroPar = 0
    while (variacoes - inteiroPar > 0):
        possibilidades.append(variacoes - inteiroPar)
        inteiroPar += 2
    return possibilidades


def funcao_menos_x(vetor_coeficientes):
    funcao_menos_x = []

    for index, coeficiente in enumerate(vetor_coeficientes):
        if (index % 2 != 0):
            funcao_menos_x.append(-coeficiente)
        else:
            funcao_menos_x.append(coeficiente)

    return funcao_menos_x


def criando_dicionario(possibilidadesNegativas, possibilidadesPositivas):
    indexMaior = max(len(possibilidadesNegativas),
                     len(possibilidadesPositivas)) - 1

    try:
        possibilidadesNegativas[indexMaior]
    except:
        while len(possibilidadesNegativas) <= indexMaior:
            possibilidadesNegativas.append([])

    try:
        possibilidadesPositivas[indexMaior]
    except:
        while len(possibilidadesNegativas) <= indexMaior:
            possibilidadesPositivas.append([])

    possiveisQuantidadeRaizes = []
    for positivas, negativas in zip(possibilidadesNegativas, possibilidadesPositivas):
        dicionario = {"positivas": positivas, "negativas": negativas}
        possiveisQuantidadeRaizes.append(dicionario)

    return possiveisQuantidadeRaizes
