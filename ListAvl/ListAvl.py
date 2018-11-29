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
            self.array[i] = []




    #trova l'insieme di appartenenza data una chiave
    def trovaInsiemeGiusto(self, key):
        for i in range(self.d):
            if(self.min + i * self.b <= key < self.min + (i + 1) * self.b):
                return i
        if(key < min):
            return self.d
        else:
            return self.d + 1

    # ritorna true se lista e false se avl
    def checkListOrAvl(self):
        pass


    #cambia lista in avl e viceversa
    def change(self):
        pass

    def insert(self, key, value):
        pos = self.trovaInsiemeGiusto(key)
        if(self.array[pos] == None):
            pass
            #crea lista con key e valore
        elif(self.checkListorAvl(self.array[pos])):
            # inserisci nella lista
            if(self.array[pos].len() == 6):
                self.change()
        else:
            pass
            #inserisci nell'avl
