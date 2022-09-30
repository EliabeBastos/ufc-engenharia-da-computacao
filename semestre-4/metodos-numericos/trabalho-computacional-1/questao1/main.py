from metodo_bairstow import metodo_bairstow
from metodo_bernoulli import estima_qraizes
from raio import localiza_raio_raizes_1, localiza_raio_raizes_2
import time

raio = 10
precisao = 0.0001
vetor_polinomios = [[-20, 3, 14.5, -7.5, 1],
                    [10, -7, -6, 1, -5, 1],
                    [-5, -3, 1, 1],
                    [-3, 4, -0.5, 1],
                    [10, 0, 6, 0, 2],
                    [8, -8, 6, -2, 1]]

for polinomio in vetor_polinomios:
    inicio = time.time()
    grau = len(polinomio) - 1

    print("\n\n\nPara o seguinte polinômio:")
    print("f(x) = ", end="")
    for index, coeficiente in enumerate(polinomio):
        if (index == grau):
            print("{}.x^({})".format(coeficiente, index))
            continue
        print("{}.x^({}) + ".format(coeficiente, index), end="")

    print("A quantidade das possíveis raízes são:")
    positivas, negativas, complexas = estima_qraizes(polinomio)
    print("Raizes positivas: {}".format(positivas))
    print("Raizes negativas: {}".format(negativas))
    print("Raizes complexas: {}".format(complexas))

    print("Raio que tem pelo menos uma raiz = ",
          localiza_raio_raizes_1(polinomio))
    print("Raio que tem todas as raizes = ", localiza_raio_raizes_2(polinomio))

    print("As raízes são: ")
    raizes = metodo_bairstow(polinomio, -raio, raio, grau, precisao)
    for index, raiz in enumerate(raizes):
        print(f"Raiz {index+1} = {raiz:.3f}")

    fim = time.time()
    print(f"Tempo de execução = {fim-inicio}")
