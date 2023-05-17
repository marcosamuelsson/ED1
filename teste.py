class No:
    def __init__(self, info):
        self.__info = info
        self.__prim = None
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
    def prim(self):
        return self.__prim
    
    @prim.setter
    def prim(self, raiz):
        self.__prim = raiz

    @property
    def prox(self):
        return self.__prox
        
    @prox.setter
    def prox(self, no):
        self.__prox = no

class Arvore:
    def __init__(self, no):
        self.__raiz = no

    def criarNo(self, info):
        novo = No(info)
        self.raiz = novo
        return novo
    
    def insere(self, pai, filho):
        filho.prox = pai.prim
        pai.prim = filho
        self.raiz = pai

    def insere_fim(self, pai, filho):
        ant = None
        p = pai.prim
        while p!=None:
            ant = p
            p = p.prox
        
        if ant == None:
            pai.prim = filho
        else:
            ant.prox = filho


    def toString(self):
        return self.__imprime(self.raiz)
    
    def __imprime(self, no):
        s = ""
        s = s + "<"
        s = s + str(no.info)
        p = no.prim
        while p != None:
            s = s + self.__imprime(p)
            p = p.prox
        s = s + ">"
        return s
    
    def pertence(self, v):
        return self.__pertence(self.raiz, v)
    
    def __pertence(self, no, v):
        if (no.info == v):
            return True
        else:
            p = no.prim
            while p != None:
                if self.__pertence(p,v):
                    return True
                p = p.prox
        return False
    
    def altura(self):
        return self.__altura(self.raiz)
    
    def __altura(self, no):
        hmax = -1
        p = no.prim
        while p != None:
            h = self.__altura(p)
            if h > hmax:
                hmax=h
            p = p.prox
        return hmax + 1
    
    def folhas(self, v):
        qtd = 0
        if v == None:
            return 0
        while v.prox != None:
            return qtd + 1
        return v
    
    def pares(self, raiz):
        v = 0
        if raiz == None:
            return 0 
        if raiz.info % 2 == 0:
            v = v + 1
        return self.pares(raiz.prim) + self.pares(raiz.prox) + v
    
    def igual(self, arv):
        p1 = self.raiz
        p2 = arv.raiz

        if p1 == p2:
            print("As árvores 1 e 2 são iguais? ", end="")
            return True
        else:
            print("As árvores 1 e 2 são iguais? ", end="")
            return False
        
    def copia(self):
        nova_arvore = Arvore(None)
        nova_arvore.raiz = self.__copia(nova_arvore, self.raiz)
        return nova_arvore

    def __copia(self, nova_arv, no):
        pai = nova_arv.criarNo(no.info)
        p = no.prim
        while p != None:
            nova_arv.insere_fim(pai, self.__copia(nova_arv, p))
            p = p.prox
        return pai


a = Arvore(None)
n1 = a.criarNo(1)
n2 = a.criarNo(2)
n3 = a.criarNo(3)
n4 = a.criarNo(4)
n5 = a.criarNo(5)
n6 = a.criarNo(6)
n7 = a.criarNo(7)
n8 = a.criarNo(8)
n9 = a.criarNo(9)
n10 = a.criarNo(10)

a.insere(n3, n4)
a.insere(n2, n5)
a.insere(n2, n3)
a.insere(n9, n10)
a.insere(n7, n9)
a.insere(n7, n8)
a.insere(n1, n7)
a.insere(n1, n6)
a.insere(n1, n2)

print(a.toString())

a2 = a.copia()
print(a2.toString())


        