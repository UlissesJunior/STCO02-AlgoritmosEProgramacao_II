print(ord('h'))
print(ord('o'))
print(ord('k'))

print(sum(map(ord, 'hokama'))) #koj
print(sum(map(ord, 'joiama')))

def hash2(s):
    mult = 1
    hashValue = 0
    for c in s:
        hashValue += mult * ord(c)
        mult += 1
    return hashValue

print(hash2('hokama'))
print(hash2('joiama'))
print(hash2('kojama')) # igual a hash('hokama')

print(hash2('ad'))
print(hash2('ga'))

class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None for i in range(size)]
        self.count = 0
        
    def hash(self, s):
        mult = 1
        hashValue = 0
        for c in s:
            hashValue += mult * ord(c)
            mult += 1
        return hashValue
    
    def put(self, key, value):
        hv = self.hash(key) % self.size
        hi = HashItem(key, value)

        # n vai funcionar se a tabela estiver cheias
        while self.slots[hv] != None:
            hv = (hv + 1) % self.size
        
        self.slots[hv] = hi
        self.count +=1
        self.check_growth()
        
    def get(self, key):
        hv = self.hash(key) % self.size
        while self.slots[hv] != None:
            if self.slots[hv].key == key:
                return self.slots[hv].value
            hv = (hv + 1) % self.size
        
        return None
    
    def growth(self):
        newTable = HashTable(self.size * 2)
        for i in range(0, self.size):
            if self.slots[i] != None:
                newTable.put(self.slots[i].key, self.slots[i].value)
        self.size = self.size * 2
        self.slots = newTable.slots
        
    def check_growth(self):
        fatorCarga = self.count / self.size
        if fatorCarga > 0.65:
            self.growth()
    
    
Table = HashTable(11)
Table.put("hokama", "c1130")
Table.put("diogo", "bla")
Table.put("rodrigo", "ble")
Table.put("jose", "bli")
Table.put("pedro", "blo")
Table.put("ad", "blu")
Table.put("ga1", "blue")
Table.put("ga2", "blue")
Table.put("ga3", "blue")
Table.put("ga4", "blue")
Table.put("ga5", "blue")
Table.put("ga6", "blue")
Table.put("ga7", "blue")
Table.put("ga8", "blue")
Table.put("ga9", "blue")

print(Table.get("hokama"))
print(Table.get("diogo"))
print(Table.get("rodrigo"))
print(Table.get("jose"))
print(Table.get("henrique"))
print(Table.get("ga"))
print(Table.get("ad"))