class metodo_ponto_fixo:
  def __init__(self, funcao):
    self.funcao = funcao
    
  def procura_raiz(self, x_inicial, erro_aceitavel = 0.01, maxIteracao = 50):
    niter = 1
    x_obtido = self.funcao(x_inicial)
    erro = abs((x_obtido-x_inicial)/x_obtido)
    while (niter < maxIteracao) and (erro>erro_aceitavel):
      x_inicial = x_obtido
      x_obtido = self.funcao(x_inicial)
      erro = abs((x_obtido-x_inicial)/x_obtido)
      niter = niter+1
    print ("Total de iterações: ", niter)
    return x_obtido