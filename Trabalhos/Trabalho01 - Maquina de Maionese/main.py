class HashTable:
    def __init__(self, size=29):
        self.size = size
        self.slots = [None] * self.size

    def hash(self, s):
        mult = 1
        hashValue = 0
        for c in s:
            hashValue += mult * ord(c)
            mult += 1
        return hashValue % self.size

    def put(self, key, value):
        index = self.hash(key)
        if self.slots[index] is None:
            self.slots[index] = BinarySearchTree()
        self.slots[index].insert(key, value)

    def get(self, key):
        index = self.hash(key)
        if self.slots[index] is None:
            return None
        return self.slots[index].search(key)

    def print_table(self):
        for i in range(self.size):
            if self.slots[i] is None:
                print("None")
            else:
                print(self.slots[i].preorder(self.slots[i].root))  

class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.recursiveInsert(self.root, key, value)

    def recursiveInsert(self, node, key, value):
        if node is None:
            return BSTNode(key, value)
        if key < node.key:
            node.left = self.recursiveInsert(node.left, key, value)
        else:
            node.right = self.recursiveInsert(node.right, key, value)
        return node

    def search(self, key):
        return self.recursiveSearch(self.root, key)

    def recursiveSearch(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.recursiveSearch(node.left, key)
        else:
            return self.recursiveSearch(node.right, key)

    def preorder(self, node):
        if node is None:
            return "None"
        return f"({node.key}, {self.preorder(node.left)}, {self.preorder(node.right)})"
    
class MenuController:
    def __init__(self):
        self.itemTable = HashTable()
        self.receitaTable = HashTable()
        self.processa_dados()
        self.handleMenu()
    
    def processa_dados(self):
        dados = []
        with open("craft.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados.append(linha.strip())

        isTitle = True
        key = ""
        ingredientes = []

        for i in range(len(dados)):
            dado = dados[i]
            if isTitle:
                key = dado
                ingredientes = []
                isTitle = False
            elif dado == "" or i == len(dados) - 1:
                if i == len(dados) - 1 and dado != "":
                    nome, qtd = dado.rsplit(" ", 1)
                    ingredientes.append((nome, int(qtd)))

                self.receitaTable.put(key, ingredientes)

                for nome_item, _ in ingredientes:
                    lista_receitas = self.itemTable.get(nome_item)
                    if lista_receitas is None:
                        self.itemTable.put(nome_item, [key])
                    else:
                        lista_receitas.append(key)

                isTitle = True
            else:
                nome, qtd = dado.rsplit(" ", 1)
                ingredientes.append((nome, int(qtd)))
        
    def handleMenu(self):
        while True:
            comando = input()
            
            if comando == "q":
                break

            if comando.startswith("r "):
                nome = comando[2:]
                print(nome)
                resultado = self.receitaTable.get(nome)
                if resultado is None:
                    print("Não encontrado")
                else:
                    for nome_item, qtd in resultado:
                        print(f"{nome_item} {qtd}")

            elif comando.startswith("i "):
                nome = comando[2:]
                print(nome)
                resultado = self.itemTable.get(nome)
                if resultado is None:
                    print("Não encontrado")
                else:
                    for rec in resultado:
                        print(rec)

            elif comando == "p r":
                self.receitaTable.print_table()

            elif comando == "p i":
                self.itemTable.print_table()
                
MenuController()