import numpy as np
import matplotlib.pyplot as plt

def grafico_funcao(inicio, fim, funcao, quant_particao = 1000):
  dominio = np.linspace(inicio, fim, quant_particao)
  imagem = []
  for elemento in dominio:
    imagem.append(funcao(elemento))
  plt.grid()
  plt.plot(dominio, imagem, label = f"Gráfico de f(x) de {inicio} e {fim}")
  plt.show();