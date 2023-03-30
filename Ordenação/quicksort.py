import criarVetorEmbaralhado

alist = criarVetorEmbaralhado.vector

# Função para o Quick Sort:

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist, primeiro, ultimo):
    if primeiro < ultimo:

        splitpoint = partition(alist, primeiro, ultimo)

        quickSortHelper(alist, primeiro, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, ultimo)

def partition(alist, primeiro, ultimo):
    pivotvalue = alist[primeiro]

    esquerda = primeiro + 1
    direita = ultimo

    done = False
    while not done:
        while esquerda <= direita and alist[esquerda] <= pivotvalue:
            esquerda = esquerda + 1
        
        while alist[direita] >= pivotvalue and direita >= esquerda:
            direita = direita - 1
        
        if direita < esquerda:
            done = True
        else:
            temp = alist[esquerda]
            alist[esquerda] = alist[direita]
            alist[direita] = temp
    
    temp = alist[primeiro]
    alist[primeiro] = alist[direita]
    alist[direita] = temp

    return direita

quickSort(alist)
print("Lista ordenada pelo algoritmo Quick Sort: ",alist)
