class FIla:
    class FilaVetor:
        def __init__(self): 
            self.__info = None
            self.__prox = None

        def FilaVetor(self, tam):
            self.vet = int[tam]
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