class Lista:

    class __NoLista:

        def __init__(self):
            self.__info = None
            self.__prox = None
        
        def getInfo(self):
            return self.__info
        
        def setInfo(self, novo_info):
            self.__info = novo_info

        #getInfo
        @property
        def info(self):
            return self.__info
        
        #setInfo
        @info.setter
        def info(self, novo_info):
            self.__info = novo_info
    
        @property
        def prox(self):
            return self.__prox
        
        @prox.setter
        def prox(self, no):
            self.__prox = no
    
    # método da classe Lista
    def __init__(self) -> None:
        self.__prim = None

    def insere(self, info):
        # instanciar novo nó
        novo = Lista.__NoLista()
        novo.info = info
        novo.prox = self.__prim
        self.__prim = novo
    
    def imprime(self):
        print("Lista Simples:", end=" ")
        p = self.__prim
        while (p != None):
            print(p.info, end=" ")
            p = p.prox
        print()

    def vazia(self):
        return self.__prim == None
    
    def ultimo(self):
        if self.vazia():
            return None
        p = self.__prim
        while (p.prox != None):
            p = p.prox
        return p
    
    def insereFim(self, valor):
        novoNo = Lista.__NoLista()
        novoNo.info = valor
        novoNo.prox = None

        ult = self.ultimo()
        if ult == None:
            self.__prim = novoNo
        else:
            ult.prox = novoNo
    
    def comprimento(self):
        if self.vazia():
            return None
        
        p = self.__prim
        i = 1
        while (p.prox != None):
            p = p.prox
            i = i + 1
        return i
    
    def __str__(self):  
        return str(self.info)
    
    def retira(self, v):
        if self.__prim.info == v:
            self.__prim = self.__prim.prox
        
        else:
            anterior = None
            corrente = self.__prim
            while corrente and corrente.info != v:
                anterior = corrente
                corrente = corrente.prox
            
            if corrente:
                anterior.prox = corrente.prox
            else:
                anterior.prox = None
        
    def libera(self):
       self.__prim = None
       self.comprimento() == 0
       
# MAIN

l1 = Lista()

l1.imprime()
l1.insereFim(8)
l1.insere(3)
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()

l1.insereFim(2131)
l1.insere(2)
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()

l1.insereFim(234)
l1.insere(1)
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()

l1.retira(1)
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()

l1.libera()
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()