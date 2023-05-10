class No:
     
    def __init__(self, info, sad, sae):
        self.info = info
        self.sad = sad
        self.sae = sae

class ArvoreBinaria:

    def __init__(self):
        self.raiz = No(None,None,None)
        self.raiz = None

    def inserir(self, v):
        Novo = No(v,None,None)
        if self.raiz == None:
            self.raiz = Novo
        else:
            atual = self.raiz
            while True:
                anterior = atual
                if v <= atual.info:
                        atual = atual.sae
                        if atual == None:
                            anterior.sae = Novo
                            return
                  
                else:
                        atual = atual.sad
                        if atual == None:
                                anterior.sad = Novo
                                return
    def buscar(self, chave):
        if self.raiz == None:
            return None 
        atual = self.raiz 
        while atual.info != chave: 
            if chave < atual.info:
                atual = atual.sae 
            else:
                atual = atual.sad 
            if atual == None:
                return None 
        return atual
     
    def proxNo(self, apaga): 
        paidoprox = apaga
        prox = apaga
        atual = apaga.sad 

        while atual != None: 
            paidoprox = prox
            prox = atual
            atual = atual.sae 
        if prox != apaga.sad: 
            paidoprox.sae = prox.sad 
            prox.sad = apaga.sad 
        return prox

    def remover(self, v):
        if self.raiz == None:
            return False 
        atual = self.raiz
        pai = self.raiz
        filho_sae = True

        while atual.info != v: 
            pai = atual
            if v < atual.info: 
                    atual = atual.sae
                    filho_sae = True 
                    atual = atual.sad 
                    filho_sae = False 
            if atual == None:
                return False 
         
        if atual.sae == None and atual.sad == None:
            if atual == self.raiz:
                    self.raiz = None 
            else:
                if filho_sae:
                        pai.sae =  None 
                else:
                        pai.sad = None 
        elif atual.sad == None:
            if atual == self.raiz:
                    self.raiz = atual.sae  
            else:
                if filho_sae:
                        pai.sae = atual.sae 
                else:
                        pai.sad = atual.sae 
         
        elif atual.sae == None:
            if atual == self.raiz:
                    self.raiz = atual.sad 
            else:
                if filho_sae:
                        pai.sae = atual.sad
                else:
                        pai.sad = atual.sad 
        else:
            prox = self.proxNo(atual)
               
            if atual == self.raiz:
                self.raiz = prox 
            else:
                if filho_sae:
                         pai.sae = prox 
                else:
                    pai.sad = prox 
            prox.sae = atual.sae 
        return True
    
    def vazia(self):
         return self.raiz == None
    
    def imprimeOrdem(self, atual):
        if atual != None:
            self.imprimeOrdem(atual.sae)
            print(atual.info,end=" ")
            self.imprimeOrdem(atual.sad)
  
    def impriemPre(self, atual):
        if atual != None:
            print(atual.info,end='')
            print("<",end='')
            self.impriemPre(atual.sae)
            self.impriemPre(atual.sad)
        print(">",end='')
       
    def imprimePos(self, atual):
        if atual != None:
            self.imprimePos(atual.sae)
            self.imprimePos(atual.sad)
            print(">",end='')
            print(atual.info,end=" ")
        print("<",end='')

    def altura(self, atual):
        if atual == None or atual.sae == None and atual.sad == None:
            return 0
        else:
            if self.altura(atual.sae) > self.altura(atual.sad):
                return  1 + self.altura(atual.sae) 
            else:
                return  1 + self.altura(atual.sad) 
  
    def folhas(self, atual):
         if atual == None:
            return 0
         if atual.sae == None and atual.sad == None:
            return 1
         return self.folhas(atual.sae) + self.folhas(atual.sad)

  
    def numNos(self, atual):
        if atual == None:
            return 0
        else:
            return  1 + self.numNos(atual.sae) + self.numNos(atual.sad)
        
        
    def pares(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.sae
        return anterior
            
    def min(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.sae
        return anterior

    def max(self):
        atual = self.raiz
        anterior = None
        while atual != None:
            anterior = atual
            atual = atual.sad
        return anterior
    
    def igual(self, arv):
        p1 = self.atual
        p2 = arv.atual

        while (p1 != None) and (p2 != None):
            if (p1.info != p2.info):
                return False
            p1 = p1.sae
            p2 = p2.sae

        if p1 == p2:
            return True
        else: 
            return False

    def percorrer(self):

        print(" Árvore em Ordem: ",end="")
        self.imprimeOrdem(self.raiz)
        
        print("\n Árvore em Pós-Ordem: ",end="")
        self.imprimePos(self.raiz)

        print("\n Árvore em Pré-Ordem: ",end="")
        self.impriemPre(self.raiz)

        print("\n Altura da arvore: %d" %(self.altura(self.raiz)))

        print(" Quantidade de folhas: %d"  %(self.folhas(self.raiz)))

        print(" Quantidade de Nós: %d" %(self.numNos(self.raiz)))


        if self.raiz != None: # se arvore nao esta vazia
            print(" A quantidade de números pare é: %d" %(((self.pares().info)%2)==0))
            print(" Valor minimo: %d" %(self.min().info))
            print(" Valor maximo: %d" %(self.max().info))

     
"""    MAIN TESTE COM MENU """
arvore = ArvoreBinaria()

opcao = 0
while opcao != 4:
    print("-----------------------------")
    print("Escolha uma opção:")
    print(" 1: Inserir Número")
    print(" 2: Excluir Número")
    print(" 3: Exibir Resultados")
    print(" 4: Sair do programa")
    print("-----------------------------")
    opcao = int(input("-- "))

    if opcao == 1:
        x = int(input(" Informe o valor -> "))
        arvore.inserir(x)

    elif opcao == 2:
        x = int(input(" Digite um número -- "))
        if arvore.remover(x) == False:
            print(" VALOR NÃO VÁLIDO")	 

    elif opcao == 3:
        arvore.percorrer()

    elif opcao == 4:
        break