import criarVetorEmbaralhado

# Python program for implementation of MergeSort

# Merges two subalistays of alist[].
# First subalistay is alist[l..m]
# Second subalistay is alist[m+1..r]


def merge(alist, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	# create temp alistays
	L = [0] * (n1)
	R = [0] * (n2)

	# Copy data to temp alistays L[] and R[]
	for i in range(0, n1):
		L[i] = alist[l + i]

	for j in range(0, n2):
		R[j] = alist[m + 1 + j]

	# Merge the temp alistays back into alist[l..r]
	i = 0	 # Initial index of first subalistay
	j = 0	 # Initial index of second subalistay
	k = l	 # Initial index of merged subalistay

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			alist[k] = L[i]
			i += 1
		else:
			alist[k] = R[j]
			j += 1
		k += 1

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		alist[k] = L[i]
		i += 1
		k += 1

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		alist[k] = R[j]
		j += 1
		k += 1

# l is for left index and r is right index of the
# sub-alistay of alist to be sorted


def mergeSort(alist, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(alist, l, m)
		mergeSort(alist, m+1, r)
		merge(alist, l, m, r)


# Driver code to test above
""" Criando uma lista de 10 números aleatórios 
que variam de 0 a 52. """
alist = criarVetorEmbaralhado.vector

n = len(alist)
print("Lista não ordenada:")
for i in range(n):
	print("%d" % alist[i],end=" ")

mergeSort(alist, 0, n-1)
print("\n\nLista ordenada pelo método Merge Sort:")
for i in range(n):
	print("%d" % alist[i],end=" ")