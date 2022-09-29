from funcao import funcao1, funcao2
from metodo_bisseccao import bisseccao
from calcula_raizes import calcula_raizes

print("Função do item A")
print(calcula_raizes(-100,100, funcao1, bisseccao, 10000))

print("Função do item B")
print(calcula_raizes(0.1, 100, funcao2, bisseccao, 10000))