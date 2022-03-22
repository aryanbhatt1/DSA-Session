# Separate Chaining

HashTable = [[] for _ in range(5)]


def Hashing(keyvalue):
    return keyvalue % len(HashTable)


def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)


def display_hash(HashTable):
    for i in range(len(HashTable)):
        print(i, end=" ")

        for j in HashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()


display_hash(HashTable)
print()
insert(HashTable, 10, 'Aryan')
insert(HashTable, 20, 'Jayesh')
insert(HashTable, 18, 'Jyothisman')
insert(HashTable, 11, 'Himanshu')
display_hash((HashTable))