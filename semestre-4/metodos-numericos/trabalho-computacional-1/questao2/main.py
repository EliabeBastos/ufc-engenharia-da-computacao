from funcao import funcao1, funcao2
from metodo_bisseccao import bisseccao
from calcula_raizes import calcula_raizes
import time

inicio = time.time()
print("Função do item A")
print("As raízes são = ", calcula_raizes(-100, 100, funcao1, bisseccao, 10000))
print("\n")
print("Função do item B")
print("As raízes são = ", calcula_raizes(0.1, 100, funcao2, bisseccao, 10000))
fim = time.time()

print("Tempo de processamento = {}".format(fim-inicio))
