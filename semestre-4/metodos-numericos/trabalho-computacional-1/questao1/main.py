from metodo_bairstow import metodo_bairstow
from metodo_bernoulli import metodo_bernoulli

raio = 10
precisao = 0.0001
vetor_polinomios = [[1, -7.5, 14.5, 3, -20],
                    [1, -5, 1, -6, -7, 10],
                    [1, 1, -3, 5],
                    [1, -0.5, 4, -3],
                    [2, 0, 6, 0, 10],
                    [1, -2, 5, -8, 8]]

for polinomio in vetor_polinomios:
    grau = len(polinomio) - 1

    print("\n\n\nPara o seguinte polinômio:")
    for index, coeficiente in enumerate(polinomio):
        print("{}.x^({}) + ".format(coeficiente, grau-index), end="")
        if (index == grau):
            print("{}".format(coeficiente))
    print("A quantidade das possíveis raízes reais são:")
    print(metodo_bernoulli(polinomio))
    print("As raízes são: ")
    print(metodo_bairstow(polinomio, -raio, raio, grau, precisao))
