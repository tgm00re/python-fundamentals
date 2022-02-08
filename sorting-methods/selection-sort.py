
from tracemalloc import start


def selectionSort(arr):
    for startingIndex in range(len(arr) - 1):
        smallest = arr[startingIndex]
        swap_index = startingIndex
        for traverseIndex in range(startingIndex, len(arr)):
            if(smallest > arr[traverseIndex]):
                smallest = arr[traverseIndex]
                swap_index = traverseIndex
        arr[startingIndex], arr[swap_index] = arr[swap_index], arr[startingIndex]

my_arr = [6,3,4,2,1,-1,0,-1]

selectionSort(my_arr)

print(my_arr)
        