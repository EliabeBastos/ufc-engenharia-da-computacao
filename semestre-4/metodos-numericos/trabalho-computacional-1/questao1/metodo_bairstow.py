import numpy as np
import math


def metodo_bairstow(vetor_coeficientes, r, s, grau, epsilon):
    xx = np.linspace(0, grau, grau+1)
    bi = []
    ci = []
    raizes = []
    for x in xx:
        bi.append(0)
        ci.append(0)
        raizes.append(0)
    id_raiz = 0
    while grau >= 3:
        igrau = grau
        bi[igrau] = vetor_coeficientes[igrau]
        while igrau > 0:
            igrau = igrau-1
            if igrau == grau-1:
                bi[igrau] = vetor_coeficientes[igrau]+r*bi[igrau+1]
            else:
                bi[igrau] = vetor_coeficientes[igrau] + \
                    r*bi[igrau+1]+s*bi[igrau+2]
        igrau = grau
        ci[igrau] = bi[igrau]
        while igrau > 1:
            igrau = igrau-1
            if igrau == grau-1:
                ci[igrau] = bi[igrau]+r*ci[igrau+1]
            else:
                ci[igrau] = bi[igrau]+r*ci[igrau+1]+s*ci[igrau+2]
        delta_s = (bi[1]*(ci[1]/ci[2])-bi[0])/(ci[2]-(ci[1]/ci[2])*ci[3])
        delta_r = (-1*bi[1]-ci[3]*delta_s)/ci[2]
        r = r+delta_r
        s = s+delta_s

        while abs(delta_r/r) > epsilon or abs(delta_s/s) > epsilon:
            igrau = grau
            bi[igrau] = vetor_coeficientes[igrau]
            while igrau > 0:
                igrau = igrau-1
                if igrau == grau-1:
                    bi[igrau] = vetor_coeficientes[igrau]+r*bi[igrau+1]
                else:
                    bi[igrau] = vetor_coeficientes[igrau] + \
                        r*bi[igrau+1]+s*bi[igrau+2]
            igrau = grau
            ci[igrau] = bi[igrau]
            while igrau > 1:
                igrau = igrau-1
                if igrau == grau-1:
                    ci[igrau] = bi[igrau]+r*ci[igrau+1]
                else:
                    ci[igrau] = bi[igrau]+r*ci[igrau+1]+s*ci[igrau+2]
            delta_s = (bi[1]*(ci[1]/ci[2])-bi[0])/(ci[2]-(ci[1]/ci[2])*ci[3])
            delta_r = (-1*bi[1]-ci[3]*delta_s)/ci[2]
            r = r+delta_r
            s = s+delta_s

        print('Valores de r e s encontrados: %f, %f' % (r, s))
        delta = r**2+4*s
        if delta > 0:
            raizes[id_raiz] = (r+math.sqrt(delta))/2
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1
            raizes[id_raiz] = (r-math.sqrt(delta))/2
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1

        else:
            raizes[id_raiz] = (r+complex(0, math.sqrt(-1*delta)))/2
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1
            raizes[id_raiz] = (r-complex(0, math.sqrt(-1*delta)))/2
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1

        grau = grau-2
        igrau = grau
        while igrau >= 0:
            vetor_coeficientes[igrau] = bi[igrau+2]
            igrau = igrau-1
    if grau == 2:
        delta = vetor_coeficientes[1]**2-4 * \
            vetor_coeficientes[2]*vetor_coeficientes[0]
        if delta >= 0:
            raizes[id_raiz] = (-1*vetor_coeficientes[1] +
                               math.sqrt(delta))/(2*vetor_coeficientes[2])
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1
            raizes[id_raiz] = (-1*vetor_coeficientes[1] -
                               math.sqrt(delta))/(2*vetor_coeficientes[2])
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1

        else:
            raizes[id_raiz] = (-1*vetor_coeficientes[1]+complex(0,
                               math.sqrt(-1*delta)))/(2*vetor_coeficientes[2])
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1
            raizes[id_raiz] = (-1*vetor_coeficientes[1]-complex(0,
                               math.sqrt(-1*delta)))/(2*vetor_coeficientes[2])
            ''' print("Raiz = ", raizes[id_raiz]) '''
            id_raiz = id_raiz+1
    else:
        raizes[id_raiz] = (-1*vetor_coeficientes[0])/vetor_coeficientes[1]
        ''' print("Raiz = ", raizes[id_raiz]) '''
    raizes.pop()
    return [-raiz for raiz in raizes]
