class FIla:
    class FilaVetor:
        def __init__(self):
            self.__n = 0
            self.__ini = 0
            self.__tam = 0
            self.__vet = []

        def FilaVetor(self, tam):
            self.vet = [tam]
            self.tam = tam
            self.ini = 0
            self.n = 0
        
    def __init__(self):
        self.__prim = None
    
    def enqueue(self, v):
        fim = 0 
        if self.n == self.tam:
            print("Erro: a capacidade de fila estourou!")
        else:
            fim = (self.ini + self.n) % self.tam
            self.vet[fim] = v
            self.n +=1
    
    def dequeue(self):
        v = 0
        if self.n == 0:
            print("ERRO: fila vazia!")
        else:
            v = self.vet[ini]
            ini = (ini + 1) % self.tam
            self.n -=1 
            return v

    def isEmpty(self):
        return self.__prim == None
    
    def reset(self):
        self.__prim = None
        self.tam == 0

f1 = FIla()

f1.enqueue(5)
print(f1)