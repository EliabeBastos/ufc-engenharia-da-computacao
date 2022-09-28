class metodo_bisseccao:
  def __init__(self, funcao):
    self.funcao = funcao
    
  def procura_raiz(self, x_inferior, x_superior, erro_aceitavel = 0.01, maxIteracao = 50):
    niter = 0
    fx_inferior = self.funcao(x_inferior)
    fx_superior = self.funcao(x_superior)
    
    x_aprox, fx_aprox, erro, niter = self.__processamento(x_inferior, x_superior, niter)
    while (niter < maxIteracao) and (erro > erro_aceitavel):
        if (fx_inferior * fx_aprox > 0) and (fx_superior * fx_aprox > 0):
            print("Escolha incorreta das estimativas")
            return 0
        if fx_inferior * fx_aprox < 0:
            x_superior = x_aprox
            fx_superior = self.funcao(x_superior)
        else:
            if fx_aprox == 0:
              return x_aprox
            x_inferior = x_aprox
            fx_inferior = self.funcao(x_inferior)
        x_aprox, fx_aprox, erro, niter = self.__processamento(x_inferior, x_superior, niter)
    print ("Total de iterações: ", niter)
    return x_aprox

  def __processamento(self, x_inferior, x_superior, niter):
      x_aprox = (x_inferior + x_superior)/2
      fx_aprox = self.funcao(x_aprox)
      erro = abs((x_aprox - x_inferior)/x_aprox)
      niter += 1
      return x_aprox, fx_aprox, erro, niter