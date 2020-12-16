#Python3 to create list of order numbers 1, 2....n                                                          
#with n being a given from the bash script or user                                                          
from quickSort import *
import time
import sys

def orderedList(number):
    return list(range(1, number+1))

# Driver code to test above
start_time = time.time()
number = int(sys.argv[1])
arr = orderedList(number)
print ("Given array is", end ="\n")
print(arr)
quickSort(arr, 0, len(arr)-1)
print ("Sorted array is:", end ="\n")
print(arr)
print("%s seconds" % (time.time() - start_time))
