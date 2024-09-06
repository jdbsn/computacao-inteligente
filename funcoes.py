def sphere(vetor):
  resultado = 0
  
  for i in vetor:
    resultado += i**2
  
  return resultado

def rastrigin(vetor):
  resultado = 0
  
  for i in vetor:
    numero = 2*3.1415*i
    p = (numero/180)*math.pi
    resultado+= (i**2) - (10 * math.cos(p)) + 10
    
  return resultado

def rosenbrock(vetor):
  resultado = 0
  
  for i in range(0,(len(vetor)-1)):
    resultado += 100*(vetor[i+1] - vetor[i]**2)**2 + (vetor[i] - 1)**2
    
  return resultado