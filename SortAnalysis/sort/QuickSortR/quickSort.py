import random
def partition(arr, low, high):
    pivot = low 
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
def partitionrand(arr, low, high):
    randpivot = random.randrange(low, high)
    arr[low], arr[randpivot] = arr[randpivot], arr[low]
    return partition(arr, low, high)
def quickSort(arr, low, high):
    if(low < high):
        pivotindex = partitionrand(arr, low, high)
        quickSort(arr, low, pivotindex-1)
        quickSort(arr, pivotindex + 1, high)
