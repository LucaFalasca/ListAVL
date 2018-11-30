from Collection.Dictionary import Dictionary
from Collection.dictTrees.avlTree import AVLTree
from Collection.linkedListDictionary import LinkedListDictionary



class ListAvl(Dictionary):
    def __init__(self, min, max, b):
        self.min = min
        self.max = max
        self.r = 6
        if(b <= self.r or (max - min) % b != 0):
            pass
            #eccezione
        else:
            self.b = b
        self.__d = (max - min) / b #da fare il modulo
        self.__array = [Dictionary(), AVLTree(), LinkedListDictionary()] #da chiedere
        for i in range(self.__d + 2):
            self.__array[i] = LinkedListDictionary()

    #trova l'insieme di appartenenza data una chiave
    def __findRightSet(self, key):
        for i in range(self.__d):
            if(self.min + i * self.b <= key < self.min + (i + 1) * self.b):
                return i
        if(key < min):
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
        if(self.__checkListOrAvl(self.__array[pos])):
            list = self.__array[pos]
            list.insert(key, value)
            if(list.theList.lenght() == 6):
                self.__array[pos] = self.__listToAvl(list)
        else:
            avl = self.__array[pos]
            avl.insert(key, value)
            elem = avl.search(key)
            avl.balInsert(elem)

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
            avl.balDelete(key)
            if(avl.size() == 5):
                self.__array[pos] = self.__avlToList(avl)

if __name__ == "__main__":
    listAvl = ListAvl(1, 17, 8)

    listAvl.insert(1, "prova1")
    listAvl.insert(2, "prova2")
    listAvl.insert(10, "prova3")
    listAvl.insert(11, "prova4")
    listAvl.insert(-4, "prova5")
    listAvl.insert(30, "prova6")

    print(listAvl.search(1))
    print(listAvl.search(4))

    listAvl.delete(1)
    print(listAvl.search(1))