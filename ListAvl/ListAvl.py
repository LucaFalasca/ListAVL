from Collection.dictTrees.avlTree import AVLTree
from Collection.list.LinkedList import ListaCollegata


class listAvl:
    def __init__(self, min, max, b):
        self.min = min
        self.max = max
        self.r = 6
        if(b <= self.r or (max - min) % b != 0):
            pass
            #eccezione
        else:
            self.b = b
        self.d = (max - min) / b #da fare il modulo
        self.array = []
        for i in range(self.d + 2):
            self.array[i] = [ListaCollegata()]




    #trova l'insieme di appartenenza data una chiave
    def __trovaInsiemeGiusto(self, key):
        for i in range(self.d):
            if(self.min + i * self.b <= key < self.min + (i + 1) * self.b):
                return i
        if(key < min):
            return self.d
        else:
            return self.d + 1

    # ritorna true se lista e false se avl
    def __checkListOrAvl(self, coll):
        if(type(coll) == ListaCollegata):
            return True
        elif(type(coll) == AVLTree):
            return False
        else:
            pass
            #eccezione


    #cambia lista in avl e viceversa
    def __change(self, coll):
        if(self.checkListOrAvl(coll)):
            avl = AVLTree()
            avl.insert()


    def insert(self, key, value):
        pos = self.trovaInsiemeGiusto(key)
        if(self.checkListorAvl(self.array[pos])):
            list = ListaCollegata(self.array[pos])
            list.addAsLast(key, value)
            if(list.lenght() == 6):
                self.change(list)
        else:
            avl = AVLTree(self.array[pos])
            avl.insert(key, value)
            #bilanciamento



