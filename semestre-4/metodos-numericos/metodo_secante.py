class metodo_secante:
  def __init__(self, funcao):
    self.funcao = funcao
    
  def procura_raiz(self, x_inferior, x_superior, erro_aceitavel = 0.01, maxIteracao = 50):
    x_obtido  = ((x_superior*self.funcao(x_inferior) - x_inferior*self.funcao(x_superior))/(self.funcao(x_inferior) - self.funcao(x_superior)))
    erro = abs((x_inferior-x_obtido)/x_obtido)
    niter = 1
    while niter < maxIteracao and erro > erro_aceitavel:
      x_superior = x_inferior
      x_inferior = x_obtido
      x_obtido  = ((x_superior*self.funcao(x_inferior) - x_inferior*self.funcao(x_superior))/(self.funcao(x_inferior) - self.funcao(x_superior)))
      erro = abs((x_inferior-x_obtido)/x_obtido)
      niter += 1
    print("Total de iterações ",niter)
    return x_obtido