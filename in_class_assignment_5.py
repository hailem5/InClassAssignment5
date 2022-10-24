#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

      
        if low <= high:
            array[low], array[high] = array[high], array[low]
           
        else:
            
            break

    array[start], array[high] = array[high], array[start]

    return high
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)

    ##code from https://stackoverflow.com/questions/18262306/quicksort-with-python

def main():
    #array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]

    #quick_sort(array, 0, len(array) - 1)
    #print(array)
    numfile = 'numbers.txt'
    fileN = open(numfile, 'r')
    reader = fileN.read()
    Remover = reader.strip('[]')
    spliter = Remover.split(',')
    fileN.close()
    setL = [eval(i) for i in spliter]
    
    quick_sort(setL,0,len(setL) - 1)
    print(setL)
    
    fileName = 'sorted.txt'
    with open(fileName,'w') as fileObject:
        return fileObject.write(str(setL))

if __name__ == "__main__":
    main()