# Python implementation of the bubble sort
def bubbleSort(A): 
    n = len(A) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if A[j] > A[j+1] : 
                A[j], A[j+1] = A[j+1], A[j] 
