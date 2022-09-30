from funcao import funcao
from metodo_bisseccao import MetodoBisseccao
import time

inicio = time.time()
metodo = MetodoBisseccao(funcao)
print(metodo.procura_raiz(-2, 1, 0.0001))
fim = time.time()

print("Tempo de processamento = {}", format(fim-inicio))
