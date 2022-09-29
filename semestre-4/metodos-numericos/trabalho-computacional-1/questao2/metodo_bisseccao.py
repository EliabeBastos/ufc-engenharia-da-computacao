def bisseccao(x_inferior, x_superior, funcao, erro_aceitavel = 0.01, maxIteracao = 50):
  niter = 0
  fx_inferior = funcao(x_inferior)
  fx_superior = funcao(x_superior)
  
  x_aprox, fx_aprox, erro, niter = processamento(x_inferior, x_superior, niter, funcao)
  while (niter < maxIteracao) and (erro > erro_aceitavel):
      if (fx_inferior * fx_aprox > 0) and (fx_superior * fx_aprox > 0):
          print("Escolha incorreta das estimativas")
          return 0
      if fx_inferior * fx_aprox < 0:
          x_superior = x_aprox
          fx_superior = funcao(x_superior)
      else:
          if fx_aprox == 0:
            return x_aprox
          x_inferior = x_aprox
          fx_inferior = funcao(x_inferior)
      x_aprox, fx_aprox, erro, niter = processamento(x_inferior, x_superior, niter, funcao)
  print ("Total de iterações: ", niter)
  return x_aprox

def processamento(x_inferior, x_superior, niter, funcao):
    x_aprox = (x_inferior + x_superior)/2
    fx_aprox = funcao(x_aprox)
    erro = abs((x_aprox - x_inferior)/x_aprox)
    niter += 1
    return x_aprox, fx_aprox, erro, niter