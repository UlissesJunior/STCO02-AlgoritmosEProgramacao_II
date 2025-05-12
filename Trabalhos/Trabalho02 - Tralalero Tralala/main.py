import csv

def lerCSV(caminhoArquivoCSV):
	criaturas = []
	with open(caminhoArquivoCSV, newline='', encoding='utf-8') as csvfile:
		leitor = csv.reader(csvfile)
		cabecalho = next(leitor)
		
		for linha in leitor:
			nome = linha[0]
			atributos = list(map(float, linha[1:]))
			criaturas.append({'nome': nome, 'atributos': atributos})
   
	return criaturas

def calcularNotas(criaturas, pesos_usuarios):
	resultados = []
 
	for usuario in pesos_usuarios:
		notas = []  
		for criatura in criaturas:
			nota = sum(c * p for c, p in zip(criatura['atributos'], usuario))
			notas.append({'nome': criatura['nome'], 'nota': nota})
		notas_ordenadas = sorted(notas, key=lambda x: (-x['nota'], x['nome']))
		resultados.append(notas_ordenadas)

	return resultados

def calcularPontuacaoFinal(resultados):
	pontuacao = {criatura['nome']: 0 for criatura in resultados[0]}
	
	for usuario in resultados:
		for pos, criatura in enumerate(usuario):
			pontuacao[criatura['nome']] += len(usuario) - pos - 1
	
	return pontuacao

def countingSortDigitoPontuacao(A, d):
    B = [None] * len(A)
    C = [0] * 10
    for a in A:
        indice = (a['pontos'] // (10 ** d)) % 10
        C[9 - indice] += 1
    for i in range(1, 10):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        a = A[i]
        indice = (a['pontos'] // (10 ** d)) % 10
        B[C[9 - indice] - 1] = a
        C[9 - indice] -= 1
    return B

def countingSortNome(A, pos):
    C = [[] for _ in range(256)] 
    for a in A:
        idx = ord(a['nome'][pos]) if pos < len(a['nome']) else 0
        C[idx].append(a)
    result = []
    for bucket in C:
        result.extend(bucket)
    return result

def radixSortNome(A):
    if not A:
        return A
    max_len = max(len(a['nome']) for a in A)
    for pos in range(max_len-1, -1, -1):
        A = countingSortNome(A, pos)
    return A

def radixSortPontuacao(A):
    if not A:
        return A
    max_ponto = max(a['pontos'] for a in A)
    D = len(str(max_ponto))
    for d in range(D):
        A = countingSortDigitoPontuacao(A, d)
    return A 

if __name__ == "__main__":
	arquivo_csv = input().strip()
	num_usuarios = int(input())
	pesos_usuarios = []
	for _ in range(num_usuarios):
		pesos = list(map(int, input().strip().split()))
		pesos_usuarios.append(pesos)
	
	criaturas = lerCSV(arquivo_csv)
	resultados = calcularNotas(criaturas, pesos_usuarios)
	pontuacao_final = calcularPontuacaoFinal(resultados)
	
	ordem_csv = {criatura['nome']: idx for idx, criatura in enumerate(criaturas)}
	
	ranking = []
	for ordem, (nome, pontos) in enumerate(pontuacao_final.items()):
		ranking.append({'nome': nome, 'pontos': pontos, 'ordem': ordem})
	
	ranking = radixSortNome(ranking)
	ranking = radixSortPontuacao(ranking)

	for item in ranking:
		print(f"{item['nome']} {item['pontos']}")