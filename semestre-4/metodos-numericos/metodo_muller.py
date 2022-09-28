import math

class metodo_muller:
  def __init__(self, funcao):
    self.funcao = funcao
    
  def procura_raiz(self, x0, x1, x2, erro_aceitavel = 0.01, maxIteracao = 50):
    niter = 0
    erro=1000
    while erro > erro_aceitavel and niter < maxIteracao:
      fx0 = self.funcao(x0)
      fx1 = self.funcao(x1)
      fx2 = self.funcao(x2)
      h0 = x1-x0
      h1 = x2-x1
      d0 = (fx1-fx0)/(x1-x0)
      d1 = (fx2-fx1)/(x2-x1)
      a = (d1-d0)/(h1+h0)
      
      b = a*h1+d1
      c = self.funcao(x2)
      if b.real>=0:
        dlt = (b**2)-4*a*c
        if dlt.real >= 0:
          delta = math.sqrt(dlt.real)
        else:
          delta = complex(0,math.sqrt(-1*dlt.real))
      else:
        dlt = (b**2)-4*a*c
        if dlt.real >=0:
          delta=-1*math.sqrt(dlt.real)
        else:delta = complex(0,-1*math.sqrt(-1*dlt.real))
                
      x3=x2+((-2*c)/(b+delta))
      erro=abs((x3-x2)/x3)
      x0=x1
      x1=x2
      x2=x3
      
      niter += 1
      
    print("Total de iterações ",niter)
    return x3