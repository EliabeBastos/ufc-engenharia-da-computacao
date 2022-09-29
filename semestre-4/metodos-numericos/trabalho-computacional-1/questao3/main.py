from funcao import funcao
from metodo_bisseccao import MetodoBisseccao

metodo = MetodoBisseccao(funcao);
print(metodo.procura_raiz(-2,1, 0.0001))