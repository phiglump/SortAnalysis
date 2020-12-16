import time
def mergeSort(A):
    if len(A) > 1:
        #Get the middle of the array
        mid = len(A)//2                                                                                                                                                                     
        #split the array down the middle into L and R
        L = A[:mid]                                                                                                                                                                           
        R = A[mid:] 
        #sort recursively thru each halves
        mergeSort(L)                                                                                                                                                                                 
        mergeSort(R)                                                                                                                                                                                
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i = i + 1
            else:
                A[k] = R[j]
                j = j + 1
            k = k + 1
        while i < len(L):
            A[k] = L[i]
            i = i + 1
            k = k + 1
        while j < len(R):
            A[k] = R[j]
            j = j + 1
            k = k + 1
