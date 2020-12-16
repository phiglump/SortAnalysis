#with n being a given from the bash script or user 
from heap import *
import time
import sys

def backwardList(end, number):
    return list(range(number, end, -1))

# Driver code to test above
start_time = time.time()
end = 0
number = int(sys.argv[1])
arr = backwardList(end, number)
print ("Given array is", end ="\n")
print(arr)
heapSort(arr)
print ("Sorted array is:", end ="\n")
print(arr)
print("%s seconds" % (time.time() - start_time))
