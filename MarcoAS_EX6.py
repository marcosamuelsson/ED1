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
        novo = No(v,None,None)
        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                anterior = atual
                if v <= atual.info:
                        atual = atual.sae
                        if atual == None:
                            anterior.sae = novo
                            return
                  
                else:
                        atual = atual.sad
                        if atual == None:
                                anterior.sad = novo
                                return
    def pertence(self, chave):
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
        print("<", end="")
        if atual != None:
            self.imprimeOrdem(atual.sae)
            print(atual.info,end="")
            self.imprimeOrdem(atual.sad)
        print(">", end="")
  
    def impriemPre(self, atual):
        print("<", end="")
        if atual != None:
            print(atual.info, end="")
            self.impriemPre(atual.sae)
            self.impriemPre(atual.sad)
        print(">", end="")
       
    def imprimePos(self, atual):
        print("<", end="")
        if atual != None:
            self.imprimePos(atual.sae)
            self.imprimePos(atual.sad)
            print(atual.info,end="")
        print(">", end="")

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
        
        
    def pares(self, raiz):
        v = 0
        if raiz == None:
            return 0
        if raiz.info % 2 == 0:
            v = v + 1
        return self.pares(raiz.sae) + self.pares(raiz.sad) + v
        
    def igual(self, arv):
        p1 = self.raiz
        p2 = arv.raiz

        if p1 == p2:
            print(" As árvpres 1 e 2 são iguais? ", end="")
            return True
        
        else:
            print(" As árvores 1 e 2 são iguais? ", end="")
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

        print(" Quantidade de pares: %d" %(self.pares(self.raiz)))

     
"""    MAIN TESTE COM MENU """
arvore = ArvoreBinaria()

opcao = 0
while opcao != 5:
    print("-----------------------------")
    print("Escolha uma opção:")
    print(" 1: Inserir Número")
    print(" 2: Excluir Número")
    print(" 3: Busca")
    print(" 4: Exibir Resultados")
    print(" 5: Sair do programa")
    print("-----------------------------")
    opcao = int(input("-- "))

    if opcao == 1:
        x = int(input(" Informe o valor: "))
        arvore.inserir(x)

    elif opcao == 2:
        x = int(input(" Digite um número: "))
        if arvore.remover(x) == False:
            print(" VALOR NÃO VÁLIDO")	 
    
    elif opcao == 3:
        x = int(input(" Digite um número: "))
        if arvore.pertence(x) != None:
            print(" Este valor pertence a árvore.")
        else:
            print(" O valor não pertence a árvore.")

    elif opcao == 4:
        arvore.percorrer()

    elif opcao == 5:
        break


""" Para testar essas funções basta encerrar o programa inicial """
p1 = ArvoreBinaria()
p2 = ArvoreBinaria()

p1.inserir(65)
p1.inserir(4)
p1.inserir(7)
p1.inserir(90)

p2.inserir(65)
p2.inserir(4)
p2.inserir(7)
p2.inserir(90)
p2.inserir(8)

print()
print(p1.igual(p2))
print()
p1.percorrer()

print()
p2.percorrer()
print()