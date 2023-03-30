from heapq import merge


class ListaDupla:

    class NoListaDupla:
        def __init__(self):
            self.prox = None
            self.antes = None

        def getInfo(self):
            return self.__info

        def setInfo(self, novo_info):
            self.__info = novo_info

        # getInfo
        @property
        def info(self):
            return self.__info

        # setInfo
        @info.setter
        def info(self, novo_info):
            self.__info = novo_info

        @property
        def prox(self):
            return self.__prox

        @prox.setter
        def prox(self, no):
            self.__prox = no

        @property
        def antes(self):
            return self.__antes

        @antes.setter
        def antes(self, no):
            self.__antes = no

    # método da classe Lista
    def __init__(self) -> None:
        self.__prim = None
        self.__fim = None

    def insere(self, info):
        # instanciar nó
        novo = ListaDupla()
        novo.info = info
        novo.prox = self.__prim
        novo.antes = None

        if self.__prim != None:
            self.__prim.antes = novo

        self.__prim = novo

    def imprime(self):
        print("Lista Duplamente Encadeada:", end=" ")
        p1 = self.__prim

        while (p1 != None):
            print(p1.info, end=" ")
            p1 = p1.prox
        print()

    def vazia(self):
        return self.__prim == None

    def busca(self, v):
        p = self.__prim
        cont = 0
        while p:
            if p.info == v:
                return p
            p = p.prox
            cont += 1
        return None

    def comprimento(self):
        if self.vazia():
            return None

        p = self.__prim
        i = 1
        while (p.prox != None):
            p = p.prox
            i = i + 1
        return i

    def ultimo(self):
        if self.vazia():
            return None

        p = self.__prim
        while (p.prox != None):
            p = p.prox
        return p

    def retira(self, v):
        p = self.busca(v)

        # caso não achar o elemento v
        if self.__prim == None:
            return

        # testa se é o primeiro nó
        if self.__prim == p:
            self.__prim = p.prox
        else:
            p.antes.prox = p.prox

        # testa se não é o útlimo
        if p.prox != None:
            p.prox.antes = p.antes

    def libera(self):
        self.__prim = None
        self.__fim = None
        self.comprimento() == 0

    def insereFim(self, v):
        novoNo = ListaDupla()
        novoNo.info = v
        novoNo.prox = None

        ult = self.ultimo()
        if ult == None:
            self.__prim = novoNo
        else:
            ult.prox = novoNo

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

    def merge(self, l):
        p = self.__prim
        q = l.__prim
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.info <= q.info:
                s = p
                p = s.prox
            else:
                s = q
                q = s.prox
            newHead = s
        while p and q:
            if p.info <= q.info:
                s.prox = p
                s = p
                p = s.prox
                
            else:
                s.prox = q
                s = q
                q = s.prox
        
        if not p :
            s.prox = q
        if not q:
            s.prox = p
        return newHead
        

# MAIN
print("Os resultados de cada operção estão à seguir: \n")

l1 = ListaDupla()
l1.insere(5)
l1.insere(2)
l1.insere(1)
l1.imprime()
print("O tamanho dessa lista é:", l1.comprimento(),"\n")


l2 = ListaDupla()
l2.insere(6)
l2.insere(4)
l2.insere(2)
l2.insere(1)
l2.imprime()
print("O tamanho dessa lista é:", l2.comprimento(),"\n")

print("A lista 1 é igual à lista 2:", l1.igual(l2),'\n')
l1.merge(l2)
l1.imprime()

print('\n')