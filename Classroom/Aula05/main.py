class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [[] for i in range(size)]
        
    def hash(self, s):
        mult = 1
        hashValue = 0
        for c in s:
            hashValue += mult * ord(c)
            mult += 1
        return hashValue
    
    def put(self, key, value):
        hv = self.hash(key) % self.size
        # supor q todo put é diferente
        self.slots[hv].append((key, value))
        
    def get(self, key):
        hv = self.hash(key) % self.size
        for (k, v) in self.slots[hv]:
            if key == k:
                return v
        return None
    
    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __getitem__(self, key):
        return self.get(key)
    
Table = HashTable(11)

Table["ferreira"] = 2024002361
print(Table["ferreira"])