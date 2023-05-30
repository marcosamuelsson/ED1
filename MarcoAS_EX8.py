from random import sample
import time

class Busca:
    def criarVetorEmbralhado(self, n):
        vet = sample(range(0, n), n)
        return vet
    
    def BuscaLinear(self, elem, vet):
        n = len(vet)
        i = 0
        for i in range(n):
            if elem == vet[i]:
                return i
        return -1
    
    def BuscaLinearCrescente(self, elem, vet):
        n = len(vet)
        i = 0
        for i in range(n):
            if elem == vet[i]:
                return i
            else:
                if elem < vet[i]:
                    return -1
        return -1
    
    def BuscaBinaria(self, elem, vet):
        n = len(vet)
        ini = 0
        fim = n - 1
        
        while ini <= fim:
            meio = int((ini + fim)/2)
            if elem < vet[meio]:
                fim = meio -1
            else:
                if elem > vet[meio]:
                    ini = meio + 1
                else:
                    return meio
        
        return -1
    
    def __BuscaBinariaRecursica(self, vet, ini, fim, elem):
        if ini < fim:
            meio = ini + int((fim -ini)/2)
            if elem < vet[meio]:
                return self.__BuscaBinariaRecursica(vet, ini, meio, elem)
            else:
                if elem > vet[meio]:
                    return self.__BuscaBinariaRecursica(vet, meio+1, fim, elem)
                else:
                    return meio
        
        return -1
    
    def BuscaBinariaRecursiva(self, elem, vet):
        return self.__BuscaBinariaRecursica(vet, 0, len(vet)-1, elem)


""" MAIN - TESTE DOS MÉTODOS DA CLASSE BUSCA  """
a = Busca()

print("BUSCA LINEAR")
lista1 = a.criarVetorEmbralhado(100000)
ini1 = time.time()
indice1 = a.BuscaLinear(999999, lista1)
fim1 = time.time()
print("A posição do elemento na lista é: ",indice1)
print(f"O tempo da execução da Busca Linear foi de {fim1-ini1} segundos")

print()
print()

print("BUSCA LINEAR CRESCENTE")
lista2 = a.criarVetorEmbralhado(100000)
lista2.sort()
ini2 = time.time()
indice2 = a.BuscaLinearCrescente(999999, lista2)
fim2 = time.time()
print("A posição do elemento na lista é: ",indice2)
print(f"O tempo da execução da Busca Linear Crescente foi de {fim2-ini2} segundos")

print()
print()

print("BUSCA BINÁRIA")
lista3 = a.criarVetorEmbralhado(100000)
lista3.sort()
ini3 = time.time()
indice3 = a.BuscaBinaria(999999, lista3)
fim3 = time.time()
print("A posição do elemento na lista é: ",indice3)
print(f"O tempo da execução da Busca Binária foi de {fim3-ini3} segundos")

print()
print()

print("BUSCA BINÁRIA RECURSIVA")
ini4 = time.time()
indice4 = a.BuscaBinariaRecursiva(999999, lista3)
fim4 = time.time()
print("A posição do elemento na lista é: ",indice4)
print(f"O tempo da execução da Busca Binária Recursiva foi de {fim4-ini4} segundos")