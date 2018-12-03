from Collection.Dictionary import Dictionary
from Collection.dictTrees.avlTree import AVLTree
from Collection.list.linkedListDictionary import LinkedListDictionary
from time import time

class ListAvl(Dictionary):
    def __init__(self, min, max, b, r = 6):
        self.r = r
        if(max <= min):
            raise MaxMinControlError()
        elif (max - min <= self.r):
            raise MaxMinSubControlError()
        else:
            self.min = min
            self.max = max
        if(b <= self.r or (max - min) % b != 0):
            raise BControlError()
        else:
            self.b = b
        self.__d = int((max - min) / b)
        self.__array = [Dictionary(), AVLTree(), LinkedListDictionary()] #da chiedere
        for i in range(self.__d - 1):
            self.__array.append(0)
        for i in range(self.__d + 2):
            self.__array[i] = LinkedListDictionary()

    #trova l'insieme di appartenenza data una chiave
    def __findRightSet(self, key):
        for i in range(self.__d):
            if(self.min + i * self.b <= key < self.min + (i + 1) * self.b):
                return i
        if(key < self.min):
            return self.__d
        else:
            return self.__d + 1

    #ritorna true se la collezione e' una lista e false se e' avl
    def __checkListOrAvl(self, coll):
        if(type(coll) is LinkedListDictionary):
            return True
        elif(type(coll) is AVLTree):
            return False
        else:
            assert "Wrong object"

    #data una lista ritorna un avl con gli elementi della lista
    def __listToAvl(self, list):
        avl = AVLTree()
        for i in range(self.r):
            elem = list.theList.popFirst()
            avl.insert(elem[list.KEY_INDEX], elem[list.VALUE_INDEX])
        return avl

    #dato un avl ritorna una lista con gli elementi dell'avl
    def __avlToList(self, avl):
        list = LinkedListDictionary()
        for i in range(self.r - 1):
            rootNode = avl.tree.root
            list.insert(rootNode.info[0], rootNode.info[1])
            avl.delete(rootNode.info[0])
        return list


    def insert(self, key, value):
        pos = self.__findRightSet(key)
        if(self.__checkListOrAvl(self.__array[pos])):
            list = self.__array[pos]
            list.insert(key, value)
            if(list.theList.lenght() == 6):
                self.__array[pos] = self.__listToAvl(list)
        else:
            avl = self.__array[pos]
            avl.insert(key, value)
            elem = avl.search(key)

    def search(self, key):
        pos = self.__findRightSet(key)
        if(self.__checkListOrAvl(self.__array[pos])):
            list = self.__array[pos]
            return list.search(key)
        else:
            avl = self.__array[pos]
            return avl.search(key)

    def delete(self, key):
        pos = self.__findRightSet(key)
        if(self.__checkListOrAvl(self.__array[pos])):
            list = self.__array[pos]
            list.delete(key)
        else:
            avl = self.__array[pos]
            avl.delete(key)
            if(avl.size() == 5):
                self.__array[pos] = self.__avlToList(avl)

    def print(self):
        for i in range(self.__d + 2):
            print("posizione " + str(i) + ":\n")
            self.__array[i].print()
            print("\n")

class BControlError(Exception):
    def __init__(self):
        super().__init__("Valore di b non coerente con le condizioni")

class MaxMinControlError(Exception):
    def __init__(self):
        super().__init__("il massimo deve essere strettamente maggiore del minimo")

class MaxMinSubControlError(Exception):
    def __init__(self):
        super().__init__("I valori di max e min non permettono nessun di valore di b valido")


if __name__ == "__main__":
    listAvl = ListAvl(1, 17, 8)

    inizio = time()
    for i in range(0, 10000):
        listAvl.insert(i, i * 2)
    fine = time() - inizio
    print(fine)

    inizio = time()
    for i in range(0, 10000):
        listAvl.search(i)
    fine = time() - inizio
    print(fine)

    inizio = time()
    for i in range(0, 10000):
        listAvl.delete(i)
    fine = time() - inizio
    print(fine)


