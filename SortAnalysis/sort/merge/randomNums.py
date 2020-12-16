#Python3 to create list of random numbers between 0 and a million n times
#with n being a given from the bash script or user
from merge import *
import time
import sys
import random

def randomList(number):
    return random.sample(range(0,1000000), number)

start_time = time.time()
number = int(sys.argv[1])
A = randomList(number)
print ("Given array is", end ="\n")
print(A)
mergeSort(A)
print("Sorted array is: ", end ="\n")
print(A)
print("%s seconds" % (time.time() - start_time))
