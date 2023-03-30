import random
import numpy as np
import criarVetorEmbaralhado

alist = criarVetorEmbaralhado.vector

# Função para o BubbleSort:

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            
bubbleSort(alist)
print("Lista ordenada pelo Algoritmo Bubble Sort: ",alist)