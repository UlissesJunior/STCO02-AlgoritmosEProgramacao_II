import csv

def parse_percent(value):
    return float(value.strip('%'))

def parse_float(value):
    return float(value)

def carregar_dados_csv(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        cabecalho = next(leitor)
        #dados.append(cabecalho) se quiser manter o cabeçalho

        for linha in leitor:
            nome = linha[0]
            roles = [r.strip() for r in linha[1].split(',')]  # ['Mid', 'Top'], por exemplo
            pickrate = parse_percent(linha[2])
            winrate = parse_percent(linha[3])
            banrate = parse_percent(linha[4])
            kills = parse_float(linha[5])
            deaths = parse_float(linha[6])
            assists = parse_float(linha[7])
            pentakills = parse_float(linha[8])

            dados.append([nome, roles, pickrate, winrate, banrate, kills, deaths, assists, pentakills])
    return dados

def CountingSortDigito(A, d):
  B = [None for _ in range(0, len(A))]
  C = [0 for _ in range(0, 10)]
  for a in A:
    indice = (a // (10**d)) % 10
    C[indice] += 1
  for i in range(1, 10):
    C[i] = C[i] + C[i-1]
  for i in range(len(A)-1, -1, -1):
    a = A[i]
    indice = (a // (10**d)) % 10
    B[C[indice] - 1] = a 
    C[indice] -= 1 
  return B


def RadixSort(A, D):
  for d in range(0, D):
    A = CountingSortDigito(A, d)
    A = list(reversed(A))
        
  return A

# Exemplo de uso
if __name__ == "__main__":
    dados = carregar_dados_csv('champs.csv')
    kdas = []
    champions = {}
    for linha in dados:
        kda = int(round(((linha[5] + linha[7]) / linha[6]), 3) * 1000)
        # kdas.append([linha[0], kda])
        kdas.append(kda)
        champions[linha[0] + str(kda)] = kda
        
    print(RadixSort(kdas, 4))   