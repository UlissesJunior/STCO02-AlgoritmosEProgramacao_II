import csv

def parse_percent(value):
  return float(value.strip('%'))

def parse_float(value):
  return float(value)

def carregar_dados_csv(caminho_arquivo):
  dados = []
  with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    
    for linha in leitor:
      nome = linha[0]
      roles = [r.strip() for r in linha[1].split(',')]
      pickrate = parse_percent(linha[2])
      winrate = parse_percent(linha[3])
      banrate = parse_percent(linha[4])
      kills = parse_float(linha[5])
      deaths = parse_float(linha[6])
      assists = parse_float(linha[7])
      
      kda = int(round(((kills + assists) / deaths), 3) * 1000)
      
      dados.append((kda, len(dados), nome))
  return dados

def counting_sort_digito(A, d):
  B = [None] * len(A)
  C = [0] * 10
  
  for a in A:
    indice = (a[0] // (10**d)) % 10
    C[indice] += 1
    
  for i in range(1, 10):
    C[i] += C[i-1]
    
  for i in range(len(A)-1, -1, -1):
    a = A[i]
    indice = (a[0] // (10**d)) % 10
    B[C[indice] - 1] = a
    C[indice] -= 1
    
  return B

def radix_sort(A, D):
  for d in range(D):
    A = counting_sort_digito(A, d)
  return A

if __name__ == "__main__":
  dados = carregar_dados_csv('champs.csv')

  dados_ordenados = radix_sort(dados, 4)
  
  campeoes_ordenados = [nome for (kda, pos, nome) in reversed(dados_ordenados)]
  
  for campeao in campeoes_ordenados:
    print(campeao)