#Python3 to create list of numbers n, n-1, n-2,....,2 , 1                                                                                                                                                               
#with n being a given from the bash script or user
from merge import *
import time
import sys

def backwardList(end, number):
    return list(range(number, end, -1))

start_time = time.time()
end = 0
number = int(sys.argv[1])
A = backwardList(end, number)
print ("Given array is", end ="\n")
print(A)
mergeSort(A)
print("Sorted array is: ", end ="\n")
print(A)
endTime = time.time()
print("%s seconds" % (endTime - start_time))
