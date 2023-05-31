class NoArvoreBinaria:
    def __init__(self, info):
        self.__info = info
        self.__sae = None
        self.__sad = None
    
    #getInfo
    @property
    def info(self):
        return self.__info
    #setInfo
    #setInfo
    @info.setter
    def info(self, novo_info):
        self.__info = novo_info

    #getSAE
    def sae(self):
        return self.__sae
    #setSAE
    def sae(self, sae):
        self.__sae = sae
    
    #getSAD
    def sad(self):
        return self.__sad
    #setSAD
    def sad(self, sad):
        self.__sad = sad
    @info.setter
    def info(self, novo_info):
        self.__info = novo_info

    #getSAE
    def sae(self):
        return self.__sae
    #setSAE
    def sae(self, sae):
        self.__sae = sae
    
    #getSAD
    def sad(self):
        return self.__sad
    #setSAD
    def sad(self, sad):
        self.__sad = sad

class ArvoreBinariaBusca:
    def __init__(self):
        self.__raiz = None

    def imprime(self):
        print("Arvore: ", end=" ")
        self.__imprime(self.__raiz)
        print()

    def __imprime(self, no):
        if no != None:
            self.__imprime(no.sae)
            print(no.info, end= " ")
            self.__imprime(no.sad)

    def busca(self, valor):
        return self.__busca(self.__raiz, valor)

    def __busca(self, r, valor):
        if r == None:
            return None
        else:
            if valor < r.info:
                return self.__busca(r.sae, valor)
            else:
                if valor > r.info:
                    return self.__busca(r.sad, valor)
                else:
                    return r
                
    def insere(self, v):
        self.__raiz = self.__insere(self.__raiz,v)
        
    def __insere(self, no, valor):
        if no == None:
            no = NoArvoreBinaria(valor)
            no.sae = None
            no.sad = None
        else:
            if valor < no.info:
                no.sae = self.__insere(no.sae, valor)
            else:
                no.sad = self.__insere(no.sad, valor)
        return no
    
    def retira(self, valor):
        self.__raiz =  self.__retira(self.__raiz, valor)

    def __retira(self, no, valor):
        if no == None:
            return None
        else:
            if valor < no.info:
                no.sae = self.__retira(no.sae, valor)
            else:
                if valor > no.info:
                    no.sad = self.__retira(no.sad, valor)
                else:
                    if no.sae == None and no.sad == None:
                        no = None
                    else:
                        if no.sae == None:
                            no = no.sad
                        else:
                            if no.sad == None:
                                no = no.sae
                            else:
                                p = no.sae
                                while p.sad != None:
                                    p = p.sad
                                no.info = p.info
                                p.info = valor
                                no.sae = self.__retira(no.sae, valor)
        return no
    
    def __str__(self):
        return str(self.info)
    

p = ArvoreBinariaBusca()
p.insere(6)
p.insere(2)
p.insere(8)
p.insere(9)
p.insere(1)
p.imprime()
p.retira(8)
p.insere(10)
p.imprime()
p.retira(2)
p.imprime()
no = p.busca(9)
print(no.info)