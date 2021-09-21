class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(0,self.max)]
    
    def get_hash(self, key):
        hash = 0
        for letter in key:
            hash += ord(letter)
        return hash % self.max
    
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        self.arr[hash] = val

    def __getitem__(self, key):
        hash = self.get_hash(key)
        return self.arr[hash]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        self.arr[hash] = None
    
    def display(self):
        print("key\tvalue")
        for i in range (0, len(self.arr)):
            print(i, self.arr[i], sep="\t", end="\n")

t = HashTable()
t['march 6'] = 280  #t.add('march 6', 280)
print(t['march 6']) #t.get("march 6")
del t['march 6']
print(t['march 6'])