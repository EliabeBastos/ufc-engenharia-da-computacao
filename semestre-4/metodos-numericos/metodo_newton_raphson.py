class metodo_newton_raphson:
  def __init__(self, funcao, derivada):
    self.funcao = funcao
    self.derivada = derivada
    
  def procura_raiz(self, x_inicial, erro_aceitavel = 0.01, maxIteracao = 50):
    x_obtido = x_inicial - (self.funcao(x_inicial)/self.derivada(x_inicial))
    niter = 1
    erro = abs((x_obtido-x_inicial)/x_obtido)
    while (niter < maxIteracao) and (erro > erro_aceitavel):
      x_inicial = x
      x_obtido = x_inicial - (self.funcao(x_inicial)/self.derivada(x_inicial))
      erro = abs((x_obtido-x_inicial)/x_obtido)
      niter += 1
    print("Total de iterações ",niter)
    return x_obtido