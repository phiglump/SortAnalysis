# Python implementation of selection sort 
def selectionSort(A):
    n = len(A)
    for i in range(n):
        index = i 
        for j in range(i+1, n):
            if A[index] > A[j]:
                index = j
                A[i], A[index] = A[index], A[i]
