#Charlie Goodrich
#11/28/17
#gnomeSort.py - models a gnome sorting algorithm

from random import randint
from time import time

N = 100 #how many numbers will be sorted

def gnomeSort(A):
    pos = 0 #position of the sorter
    while pos < len(A):
        if pos == 0 or A[pos] >= A[pos-1]:
            pos += 1
        else:
            A[pos], A[pos-1] = A[pos-1], A[pos] #swapping the numbers
            pos -= 1
    return A

if __name__ == '__main__':
    
    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
        
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = gnomeSort(numbers)
    t2 = time()
       
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
    
