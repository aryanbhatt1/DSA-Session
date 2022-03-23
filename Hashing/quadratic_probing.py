# quadratic Probing
class HashTable:

    def __init__(self, size):
        self.size = size
        self.hashtable = self.create_buckets()

    def create_buckets(self):
        return [None] * self.size

    def hash(self, key):

        index = key % len(self.hashtable)

        if self.hashtable[index] == None:
            return index
        else:
            i = 1
            while self.hashtable[index] != None:
                index = (index + (i ** 2)) % len(self.hashtable)
                i += 1

            return index

    def insert(self, key):

        index = self.hash(key)
        self.hashtable[index] = key

    def print_hashtable(self):
        for x in range(len(self.hashtable)):
            print("{}  {}".format(x, self.hashtable[x]))


ht = HashTable(10)
ht.insert(10)
ht.insert(20)
ht.insert(15)
ht.insert(5)
ht.insert(26)
ht.print_hashtable()