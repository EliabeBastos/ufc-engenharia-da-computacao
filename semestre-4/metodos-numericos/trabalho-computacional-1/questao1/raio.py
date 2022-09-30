def localiza_raio_raizes_1(coeficientes):
    vet_coef = []
    for coeficiente in coeficientes:
        if (coeficiente != 0):
            vet_coef.append(coeficiente)
    n = len(vet_coef) - 1
    pho1 = n*abs(vet_coef[0]/vet_coef[1])
    phon = (abs(vet_coef[0]/vet_coef[-1]))**(1/n)
    r1 = min([pho1, phon])
    return r1


def localiza_raio_raizes_2(vet_coef):
    vref = 0
    for i in range(0, len(vet_coef) - 1):
        if abs(vet_coef[i]/vet_coef[-1]) > vref:
            vref = abs(vet_coef[i]/vet_coef[-1])
    return 1+vref
