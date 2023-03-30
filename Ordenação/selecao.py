""" Menu de Seleção dos Métodos Sort's """

print(
    """ Menu:
    [1] BUBLLE SORT
    [2] MERGE SORT
    [3] QUICK SORT
    """
)

escolha = int(input("Escolha umas das opções acima:"))

def opcao():
    if escolha == 1:
        import bubblesort
    
    elif escolha == 2:
        import mergesort
    
    elif escolha == 3:
        import quicksort
    
    else:
        print("Número Inválido...")

if __name__ == "__main__":
    opcao()