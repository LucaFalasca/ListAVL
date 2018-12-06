import math
import pstats

from Collection.Dictionary import Dictionary
from Collection.dictTrees.avlTree import AVLTree
from Collection.list.linkedListDictionary import LinkedListDictionary
from time import time
from random import randint
import cProfile

class ListAvl(Dictionary):
    def __init__(self, min, max, b, r =6):
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
        self.__array = []
        for i in range(self.__d + 2):
            self.__array.append(LinkedListDictionary())

    #trova l'insieme di appartenenza data una chiave
    def __findRightSet(self, key):
        """
        for i in range(self.__d):
            if(self.min + i * self.b <= key < self.min + (i + 1) * self.b):
                return i
        """
        if(key < self.min):
            return self.__d
        elif(key >= self.max):
            return self.__d + 1
        else:
            return int((key - self.min) / self.b)

    #ritorna true se la collezione e' una lista e false se e' avl
    def __checkListOrAvl(self, coll):
        isinstance(coll, Dictionary)
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

def tripleGenerator():
    v = []
    b = randint(7, 1000)
    subMaxMin = b * randint(1, 50)
    max = subMaxMin + randint(-subMaxMin, subMaxMin)
    v.append(max - subMaxMin)
    v.append(max)
    v.append(b)
    return v

def tripleGeneratorOriented(v):
    n = len(v)
    sommaDistanza = 0
    for i in range(n - 1):
       sommaDistanza += abs(v[i] - v[i + 1])
    mediaDistanza = int(sommaDistanza / (n - 1))
    somma = 0
    for i in range(n):
        somma += v[i]
    media = int(somma / n)
    newN = int(math.sqrt(n))**2
    max = media + newN/2
    min = media - newN/2
    b = math.sqrt(newN)
    return [min, max, b]

def tripleGeneratorOrientedV2(v, q):
    n = len(v)

    #distanza media
    sommaDistanza = 0
    for i in range(n - 1):
        sommaDistanza += abs(v[i] - v[i + 1])
    distanzaMedia = int(sommaDistanza / (n - 1))

    if(distanzaMedia >= 2):
        b = 4**2 * (int(distanzaMedia / 4)) #perchè 4 * 2 fa 8 > 6
    else:
        b = 6
    maxMinSub = b * int(n * distanzaMedia / b)
    minimo = min(v)
    max = maxMinSub + minimo
    return [minimo, max, b]

def calculateTime(n, distanza, listAvl):
    v = []
    r = int((n * distanza) / 2)
    start = time()
    for i in range(-r, r, distanza):
        listAvl.insert(i, i)
    v.append(time() - start)

    listAvl.print()

    start = time()
    for i in range(-r, r, distanza):
        listAvl.search(i)
    v.append(time() - start)

    start = time()
    for i in range(-r, r, distanza):
        listAvl.delete(i)
    v.append(time() - start)

    return v


def calculateTimeDictionaryPython(n, distanza, dict):
    v = []
    r = int((n * distanza) / 2)
    start = time()
    for i in range(-r, r, distanza):
        dict.update({i : i})
    v.append(time() - start)

    start = time()
    for i in range(-r, r, distanza):
        dict.get(i)
    v.append(time() - start)

    start = time()
    for i in range(-r, r, distanza):
        dict.pop(i)
    v.append(time() - start)

    return v


if __name__ == "__main__":


    # #Tripla Casuali
    # v = tripleGenerator()
    # print(v)
    # listAvl = ListAvl(v[0], v[1], v[2])
    #
    # print("=============================\nTripla casuale\n=============================\n")
    # n = 2500
    # distanza = 20
    # for k in range(6):
    #     print("-----------------------")
    #     print("Numero elementi: " + str(n))
    #     print("-----------------------\n")
    #     for i in range(3):
    #         print("\t-----------------------")
    #         print("\tDistanza: " + str(distanza**i))
    #         print("\t-----------------------\n")
    #         # results = calculateTime(n, distanza**i, listAvl)
    #         # print("\t\tInsert: " + str(results[0]))
    #         # print("\t\tSearch: " + str(results[1]))
    #         # print("\t\tDelete: " + str(results[2]))
    #         cProfile.run('for i in range(0, n, distanza**i): listAvl.insert(i, i)', 'fileOutput')
    #         p = pstats.Stats('fileOutput')
    #         p.strip_dirs().sort_stats("time").print_stats()
    #         print("\n")
    #     n *= 2
    #
    #
    # print(2000 % int(math.log(2000)))
    #Tripla ottimizzata
    print("=============================\nTripla orientata\n=============================\n")
    n = 2500
    distanza = 20
    for k in range(6):
        print("-----------------------")
        print("Numero elementi: " + str(n))
        print("-----------------------\n")
        for i in range(3):
            elementi = []
            r = int((n * distanza**i) / 2)
            for j in range(-r, r, distanza**i):
                elementi.append(j)
            v = tripleGeneratorOrientedV2(elementi, 0)
            listAvl = ListAvl(v[0], v[1], v[2])
            print("\t-----------------------")
            print("\tDistanza: " + str(distanza ** i))
            print("\t-----------------------\n")
            results = calculateTime(n, distanza ** i, listAvl)
            print("\t\tInsert: " + str(results[0]))
            print("\t\tSearch: " + str(results[1]))
            print("\t\tDelete: " + str(results[2]))
            print("\n")
        n *= 2

    # #Tripla con D piccolo
    # listAvl = ListAvl(0, 7, 7)
    #
    # print("=============================\nTripla con D Piccolo\n=============================\n")
    # n = 2500
    # distanza = 20
    # for k in range(6):
    #     print("-----------------------")
    #     print("Numero elementi: " + str(n))
    #     print("-----------------------\n")
    #     for i in range(3):
    #         print("\t-----------------------")
    #         print("\tDistanza: " + str(distanza ** i))
    #         print("\t-----------------------\n")
    #         results = calculateTime(n, distanza ** i, listAvl)
    #         print("\t\tInsert: " + str(results[0]))
    #         print("\t\tSearch: " + str(results[1]))
    #         print("\t\tDelete: " + str(results[2]))
    #         print("\n")
    #     n *= 2
    #
    # #Tripla con D grande
    # listAvl = ListAvl(0, 7 * 1000, 7)
    #
    # print("=============================\nTripla con D grande\n=============================\n")
    # n = 2500
    # distanza = 20
    # for k in range(6):
    #     print("-----------------------")
    #     print("Numero elementi: " + str(n))
    #     print("-----------------------\n")
    #     for i in range(3):
    #         print("\t-----------------------")
    #         print("\tDistanza: " + str(distanza ** i))
    #         print("\t-----------------------\n")
    #         results = calculateTime(n, distanza ** i, listAvl)
    #         print("\t\tInsert: " + str(results[0]))
    #         print("\t\tSearch: " + str(results[1]))
    #         print("\t\tDelete: " + str(results[2]))
    #         print("\n")
    #     n *= 2
    #
    #
    # #Dizionario
    # dict = dict()
    #
    # print("=============================\nDizionario\n=============================\n")
    # n = 2500
    # distanza = 20
    # for k in range(6):
    #     print("-----------------------")
    #     print("Numero elementi: " + str(n))
    #     print("-----------------------\n")
    #     for i in range(3):
    #         print("\t-----------------------")
    #         print("\tDistanza: " + str(distanza ** i))
    #         print("\t-----------------------\n")
    #         results = calculateTimeDictionaryPython(n, distanza ** i, dict)
    #         print("\t\tInsert: " + str(results[0]))
    #         print("\t\tSearch: " + str(results[1]))
    #         print("\t\tDelete: " + str(results[2]))
    #         print("\n")
    #     n *= 2
