from Collection.Dictionary import Dictionary
from Collection.dictTrees.avlTree import AVLTree
from Collection.linkedListDictionary import LinkedListDictionary
from Collection.list.LinkedList import ListaCollegata


class listAvl(Dictionary):
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
        self.array = [Dictionary(), AVLTree(), LinkedListDictionary()] #da chiedere
        for i in range(self.d + 2):
            self.array[i] = LinkedListDictionary()

    #trova l'insieme di appartenenza data una chiave
    def __findRightSet(self, key):
        for i in range(self.d):
            if(self.min + i * self.b <= key < self.min + (i + 1) * self.b):
                return i
        if(key < min):
            return self.d
        else:
            return self.d + 1

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
            avl.balInsert(elem)
        return avl

    #dato un avl ritorna una lista con gli elementi dell'avl
    def __avlToList(self, avl):
        list = LinkedListDictionary()
        for i in range(self.r - 1):
            rootNode = avl.tree.root
            list.insert(rootNode.info[0], rootNode.info[1])
            avl.delete(rootNode.info[0])
            avl.balDelete(rootNode)
        return list


    def insert(self, key, value):
        pos = self.__findRightSet(key)
        if(self.__checkListOrAvl(self.array[pos])):
            list = self.array[pos]
            list.insert(key, value)
            if(list.theList.lenght() == 6):
                self.array[pos] = self.__listToAvl(list)
        else:
            avl = self.array[pos]
            avl.insert(key, value)
            elem = avl.search(key)
            avl.balInsert(elem)

    def search(self, key):
        pos = self.__findRightSet(key)
        if(self.__checkListOrAvl(self.array[pos])):
            list = self.array[pos]
            list.search(key)
        else:
            pass



    def delete(self, key):
        pos = self.__findRightSet(key)
        if(self.__checkListOrAvl(self.array[pos])):
            list = self.array[pos]
            list.delete(key)
        else:
            avl = self.array[pos]
            avl.delete(key)
            avl.balDelete(key)
            if(avl.size() == 5):
                self.array[pos] = self.__avlToList(avl)



