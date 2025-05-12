class HashTable:
	def __init__(self, size):
		self.size = size
		self.slots = [[] for i in range(size)]
		
	def hash(self, s):
		mult = 0
		hash_value = 0
		for c in s[:3]:
			c.lower()
			hash_value += (123**mult) * ord(c)
			mult += 1
		return hash_value
		
	def put(self, key):
		hv = self.hash(key) % self.size
		#supor que todo put Ã© diferente
		self.slots[hv].append((key))
	
	def parserKey(self, key):
		dic = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'], 'o': ['0'], 's': ['5', '$'], 'h': ['#'], 'k': ['<', 'x']}
	
		combinacoes = [key] 

		antes = 0
		depois = 1
		for k in range (len(key)):
			if dic[key[k]]:
				for letra in dic[key[k]]:
					newKey = key[:antes] + letra + key[depois:]
					combinacoes.append(newKey)
			antes +=1
			depois +=1
		
		print(combinacoes)
		return combinacoes

	def get(self, key):
		hv = self.hash(key) % self.size
		nomesEncontrados = [] 
		chavesEncontradas = []

		for k in self.slots[hv]:
			if key[:3] == k[:3]:
				chavesEncontradas = self.parserKey(key[:3])
		
		print(chavesEncontradas)
		for k in self.slots[hv]:
			if k[:3] in chavesEncontradas:
				print(k[:3])
				nomesEncontrados.append(k)
		
		if nomesEncontrados:
			return nomesEncontrados

		return None


Table = HashTable(997)

nomes_invocadores = []
with open("invocadores.txt", "r", encoding="utf-8") as arquivo:
	for linha in arquivo:
		nome = linha.strip()  # Remove espaÃ§os em branco e quebras de linha
		if nome:  # Garante que nÃ£o adiciona linhas vazias
			Table.put(nome)


nome_busca = input()

while nome_busca != "-1":
		resultado = Table.get(nome_busca)
		if resultado:
				print(f"Nome encontrado: {resultado}")
		else:
				print("Nome nÃ£o encontrado.")
		nome_busca = input()



	
"""
'a': ['4', '@'],
'e': ['3'],
'i': ['1', '!'],
'o': ['0'],
's': ['5', '$'],
'h': ['#'],
'k': ['<', 'x'],
"""