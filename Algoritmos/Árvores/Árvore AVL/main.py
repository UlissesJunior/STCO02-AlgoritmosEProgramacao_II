class node:
  def __init__(self, dado):
    self.dado = dado
    self.esq = None
    self.dir = None
    self.altura = 0
    
def altura(y):
  if y == None:
    return -1
  return y.altura
    
def rotacaoDireita(y):
  x = y.esq
  y.esq = x.dir
  x.dir = y
  
  y.altura = max(altura(y.esq), altura(y.dir)) + 1
  x.altura = max(altura(x.esq), altura(x.dir)) + 1
  
  return x
  
  
def rotacaoEsquerda(y):
  x = y.dir
  y.dir = x.esq
  x.esq = y
  
  y.altura = max(altura(y.esq), altura(y.dir)) + 1
  x.altura = max(altura(x.esq), altura(x.dir)) + 1
  
  return x
  
#FB = FATOR DE BALANCEAMENTO
def fb(y):
  return altura(y.esq) - altura(y.dir)
  
def insere(y, dado):
  if y == None:
    return node(dado)
    
  if dado < y.dado:
    y.esq = insere(y.esq, dado)
    #verificar se deslanceou para esquerda
    if fb(y) == 2:
      if dado > y.esq.dado:
        #inseriu na direita da esquerda
        y.esq = rotacaoEsquerda(y.esq)
      y = rotacaoDireita(y) 
  elif dado > y.dado:
    y.dir = insere(y.dir, dado)
    if fb(y) == -2:
      #verificar se inseriu na esquerda da direita
      if dado < y.dir.dado:
        y.dir = rotacaoDireita(y.dir)
      y = rotacaoEsquerda(y)
      
  else:
    print("dado igual")
    #tratar esse caso
    return y
    
 #corrigir a altura de y
  y.altura = max(altura(y.dir), altura(y.esq)) + 1
 
  return y

def imprime(arvore, nivel=0, prefixo="Raiz: "):
    if arvore is not None:
        print(" " * (4 * nivel) + prefixo + str(arvore.dado))
        imprime(arvore.esq, nivel + 1, "E: ")
        imprime(arvore.dir, nivel + 1, "D: ")
  
T = None
T = insere(T, 10)
T = insere(T, 33)
T = insere(T, 42)
T = insere(T, 49)
T = insere(T, 50)


imprime(T)