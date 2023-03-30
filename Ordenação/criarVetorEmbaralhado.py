import numpy as np
from random import sample

x = int(input("Digite a quantidade de dados de entrada:"))

vector = sample(range(0, x), x)
print(vector)