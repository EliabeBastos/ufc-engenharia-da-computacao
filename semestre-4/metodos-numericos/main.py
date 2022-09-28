from metodo_bisseccao import metodo_bisseccao
from funcao import funcao, primeira_derivada
from grafico import grafico_funcao
from metodo_falsa_posicao import metodo_falsa_posicao
from metodo_ponto_fixo import metodo_ponto_fixo
from metodo_newton_raphson import metodo_newton_raphson
from metodo_secante import metodo_secante
from metodo_muller import metodo_muller

metodo1 = metodo_bisseccao(funcao)
print(metodo1.procura_raiz(1,2))

metodo2 = metodo_falsa_posicao(funcao)
print(metodo2.procura_raiz(1,2))

metodo3 = metodo_ponto_fixo(funcao)
print(metodo3.procura_raiz(-3,2))

metodo4 = metodo_newton_raphson(funcao, primeira_derivada)
print(metodo4.procura_raiz(0,2))

metodo5 = metodo_secante(funcao)
print(metodo5.procura_raiz(0,2))

metodo6 = metodo_muller(funcao)
print(metodo6.procura_raiz(0,2,3))

grafico_funcao(-5,5,funcao, 3000)