class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(0,self.max)]
    
    def get_hash(self, key):
        hash = 0
        for letter in key:
            hash += ord(letter)
        return hash % self.max
    
    def __setitem__(self, key, val):
        hash = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[hash].append((key, val))

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash]):
            if element[0] == key:
                del self.arr[hash][idx]
    
    def display(self):
        print("key\tvalue")
        for i in range (0, len(self.arr)):
            print(i, self.arr[i], sep="\t", end="\n")

t = HashTable()
t['march 6'] = 280
t['march 5'] = 289
t['may 1'] = 290
t['march 6'] = 291
t['march 6'] = 292
print(t['march 5'])
print(t.get_hash('march 5'))
del t['may 1']
print(t.arr)