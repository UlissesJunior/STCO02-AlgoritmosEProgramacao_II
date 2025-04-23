def selectionSort(lista):
    for i in range(len(lista) - 1, 0, 1):
        maior = 0
        for j in range(1, i + 1):
            if lista[j] > lista[maior]:
                maior = j
        aux = lista[i]
        lista[i] = lista[maior]
        lista[maior] = aux

class MaxHeap:
    def __init__(self, lista):
        self.dados = lista
        self.tamanho = len(lista)
        self.constroiHeap()
        
    def constroiHeap(self):
        for i in range(self.tamanho // 2 - 1, -1, -1):
            self.desceHeap(i)
            
    def heapSort(self):
        for i in range(self.tamanho - 1, 0, -1):
            self.dados[0], self.dados[self.tamanho - 1] = self.dadps[self.tamanho - 1], self.dados[0]
            self.tamanho -= 1
            self.desceHeap(0)

    def inserir(self, valor):
        self.dados.append(valor)
        self.sobeHeap(self.tamanho)
        self.tamanho += 1

    def sobeHeap(self, i):
        if i == 0:
            return
        
        pai = (i-1) // 2
        
        if self.dados[i] > self.dados[pai]:
            self.dados[i], self.dados[pai] = self.dados[pai], self.dados[i]
    
    def desceHeap(self, i):
        esq = 2*i + 1
        dir = 2*i + 2
        maior = -1
        if esq <= self.tamanho - 1:
            maior = esq
        if dir <= self.tamanho - 1 and self.dados[dir] > self.dados[esq]:
            maior = dir
        if maior != -1 and self.dados[maior] > self.dados[i]:
            self.dados[i], self.dados[maior] = self.dados[maior], self.dados[i]
            self.desceHeap(maior)
            
            
    def remover(self):
        if self.tamanho == 0:
            return None
        
        maximo = self.dados[0]
        self.dados[0] = self.dados[self.tamanho - 1]
        self.dados.pop()
        self.tamanho -= 1
        
        if self.tamanho > 0:
            self.desceHeap(0)
        
        return maximo
    
    def peek(self):
        return self.dados[0]

lista = [18, 1, 6, 33, 42, 31]
H = MaxHeap(lista)
print(H.dados)