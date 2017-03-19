import string

class BloomFilter:
    
    def __init__(self, bits, number_hashes):
        self.bits = bits
        self.number_hashes = number_hashes
        self.bit_set = [0] * bits
        
        
        
    def add(self, string):
        for filler in range(self.number_hashes):
            result = hash(string + str(filler)) % self.bits
            self.bit_set[result] = 1
            
    def __contains__(self, string):
        for filler in range(self.number_hashes):
            result = hash(string + str(filler)) % self.bits
            if self.bit_set[result] == 0:
                return False
        return True
    
filter = BloomFilter(1100000, 7)

lines = open("wordsEn.txt").read().splitlines()
for line in lines:
    filter.add(line)
    
file = open("declaration.txt", "r")
file = file.read()
words = [word.strip(string.punctuation).lower() for word in file.split()]

dup = []
for word in words:
    if word not in dup:
        dup.append(word)
        
        
for word in dup:
    if word not in filter:
        print(word, "  ......not in dictionary")