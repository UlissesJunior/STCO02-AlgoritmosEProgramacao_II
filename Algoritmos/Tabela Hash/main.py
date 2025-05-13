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
        if fatorCarga > 0.7:
            self.growth()