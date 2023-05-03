class ArvoreBinaria:

    class NoArvoreBinaria:
        def __init__(self, info):
            self.__info = info
            self.__sae = None
            self.__sad = None

        #INFO
        def getInfo(self):
            return self.__info

        def setInfo(self, new_info):
            self.__info = new_info
        
        #SAE
        def getSae(self):
            return self.__sae
        
        def setInfo(self, new_sae):
            self.__sae = new_sae
        
        #SAD
        def getSad(self):
            return self.__sad
        
        def setSad(self, new_sad):
            self.__sad = new_sad

        #getInfo  
        @property
        def info(self):
            return self.__info
        #setInfo
        @info.setter
        def info(self, new_info):
            self.__info = new_info
        
        #getSae
        @property
        def sae(self):
            return self.__sae
        #setSae
        @sae.setter
        def sae(self, new_sae):
            self.__sae = new_sae
        
        #getSad
        @property
        def sad(self):
            return self.__sad
        #setSad
        @sad.setter
        def sad(self, new_sad):
            self.__sad = new_sad

        def toStrig(self):
            return self.__imprimePre(self.__raiz)
        
        def __imprimePre(self, no):
            s = ("")
            s = s + "<"

            if (no != None):
                s = s + no.info
                s =  s + self.__imprimePre(no.sae)
                s = s + self.__imprimePre(no.dir)
            s = s + ">"
            return set
        
    def __init__(self, info):
            self.__raiz = None
            self.prim = None
            self.prox = None
            self.info = info
    
    def NoArvore(self, info,sa):
        self.info = info
        self.prox = sa.prim
        self.prim = sa

    def insere(self, v, sae, sad):
        no = self.NoArvoreBinario(v, sae, sad)
        self.__raiz = no
        return no
    
    def vazia(self):
        return (self.__raiz == None)
    
    
    def pertence(self, v):
        return self.__pertence(self.__raiz, v)
    
    def __pertence(self, no, v):
        if no.info == v:
            return True
        else:
            p = no.prim
            while p != None:
                if self.__pertence(p, v):
                    return True
                p = p.prox
        return False
    
    def altura(self):
        return self.__altura(self.__raiz)
    
    def __altura(self, no):
        hmax = -1
        p = no.prim

        while p != None:
            h = self.__altura(p)
            if h > hmax:
                hmax = h
            p = p.prox
        return hmax + 1
     
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