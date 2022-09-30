def estima_qraizes(vet_coef):
    quantidadeVariacoes = 0
    i = 0
    j = 1
    while i < len(vet_coef)-1 and j < len(vet_coef):
        if vet_coef[i]*vet_coef[j] < 0:
            quantidadeVariacoes += 1
            i = i+1
            j = j+1
        elif vet_coef[i]*vet_coef[j] == 0:
            if vet_coef[j] == 0:
                j = j+1
            else:
                i = i+1
        else:
            i = i+1
            j = j+1

    raizesPositivas = []
    for i in range(0, quantidadeVariacoes+1):
        if (quantidadeVariacoes - i) % 2 == 0:
            raizesPositivas.append(i)

    quantidadeVariacoes = 0
    i = 0
    j = 1
    for k in range(0, len(vet_coef)):
        vet_coef[k] = vet_coef[k]*((-1)**k)

    while i < len(vet_coef)-1 and j < len(vet_coef):
        if vet_coef[i]*vet_coef[j] < 0:
            quantidadeVariacoes += 1
            i = i+1
            j = j+1
        elif vet_coef[i]*vet_coef[j] == 0:
            if vet_coef[j] == 0:
                j = j+1
            else:
                i = i+1
        else:
            i = i+1
            j = j+1

    raizesNegativas = []
    for i in range(0, quantidadeVariacoes+1):
        if (quantidadeVariacoes - i) % 2 == 0:
            raizesNegativas.append(i)

    raizesComplexas = []
    grau = len(vet_coef)-1
    for i in raizesPositivas:
        for j in raizesNegativas:
            raizesComplexas.append(grau - i - j)

    return raizesPositivas, raizesNegativas, raizesComplexas
