# Double Hashing_Session_2
import math


class HashTable:
    def __init__(self, size):
        self.size = size
        self.num = 5
        self.table = list(0 for i in range(self.size))
        self.comparisons = 0
        self.prime = self.get_prime(len(self.table))
        self.elementCount = 0

    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    def get_prime(self, length):
        for i in range(length - 1, 1, -1):
            flag = 0
            for j in range(2, math.floor(math.sqrt(i))):
                if i % j == 0:
                    flag += 1
            if flag == 0:
                return i
        return 3

    def h1(self, element):
        return element % self.size

    def h2(self, element):
        return self.prime - (element % self.prime)

    def doubleHashing(self, element, position):
        posFound = False
        limit = 50
        i = 2
        while i <= limit:
            newPosition = (self.h1(element) + i * self.h2(element)) % self.size
            if self.table[newPosition] == 0:
                posFound = True
                break
            else:
                i += 1
        return posFound, newPosition

    def insert(self, element):
        if self.isFull():
            print("Hash Table Full")
            return False
        posFound = False
        position = self.h1(element)
        if self.table[position] == 0:
            self.table[position] = element
            print(str(position) + " " + str(element))
            isStored = True
            self.elementCount += 1

        else:
            while not posFound:
                print("Collision has occured for element " + str(element) + " at position " + str(
                    position) + " finding new Position.")
                posFound, position = self.doubleHashing(element, position)
                if posFound:
                    self.table[position] = element
                    self.elementCount += 1
        return posFound

    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " " + str(self.table[i]))
        print("The number of element is the Table are : " + str(self.elementCount))


table1 = HashTable(14)
table1.insert(12)
table1.insert(26)
table1.insert(31)
table1.insert(17)
table1.insert(90)
table1.insert(28)
table1.insert(88)
table1.insert(40)
table1.insert(77)
table1.display()
