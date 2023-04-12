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
    
    
    def igual(self, l):
        p1 = self.__prim
        p2 = l.__prim

        while (p1 != None) and (p2 != None):
            if (p1.info != p2.info):
                return False
            p1 = p1.prox
            p2 = p2.prox

        if p1 == p2:
            return True
        else:
            return False
        
    def imprimeRecurisvo(self):
        self.__imprimeRecursivoAux(self.__prim)
    
    def __imprimeRecursivoAux(self, l):
        if self.vazia():
            return False
        
        if l != None:
            print(l.info)
            print(self.__imprimeRecursivoAux(l.prox))
    
    def retiraRecursivo(self, v):
        prim = self.__retiraRecurivoAux(self.__prim, v)

    def __retiraRecurivoAux(self, l, v):
        if l != None:
            if l.info == v:
                l = l.prox
            else:
                l.prox = self.__retiraRecurivoAux(l.prox, v)
        return l

    def igualRecursivo(self, l):
        return self.__igualRecursivoAux(self.__prim, l.__prim)

    def __igualRecursivoAux(self, l1, l2):
        if (l1 == None) and (l2 == None):
            return True
        else:
            if (l1 == None) or (l2 == None):
                return False
            else:
                return ((l1.info == l2.info) and 
                        self.__igualRecursivoAux(l1.prox, l2.prox)) 

# MAIN

l1 = Lista()
l2 = Lista()

l1.imprime()
l1.insereFim(8)
l1.insere(3)
l1.imprime()
l1.retiraRecursivo(8)
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

l1.imprimeRecurisvo()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()

l1.retira(1)
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()

l2.insere(3)
l2.insere(8)
l2.insere(6676)
l2.insere(9)
l2.insereFim(0)
l2.imprime()
print()

print("(Recursivo)A lista 1 é igual a lista 2? ", l1.igualRecursivo(l2))
print("(Sem Recursividade) A lista 1 é igual a lista 2?", l1.igual(l2))
print()

l1.libera()
l1.imprime()
tamanho = l1.comprimento()
print("Tamanho da lista:", tamanho)
print()