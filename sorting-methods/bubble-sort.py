#bubble sort implementation

def bubbleSort(arr):
    arrLength = len(arr)
    for i in range(arrLength -  1):
        for k in range(i + 1, arrLength):
            if(arr[i] > arr[k]):
                arr[i], arr[k] = arr[k], arr[i]

myArr = [1,2,3,-1]

bubbleSort(myArr)
print(myArr)