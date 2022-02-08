
def insertionSort(arr):
    for i in range(1, len(arr)):
        current_val = arr[i]
        swap_index  = i - 1
        while(current_val < arr[swap_index] and swap_index >= 0):
            arr[swap_index + 1] = arr[swap_index]
            swap_index -= 1
        arr[swap_index + 1] = current_val


my_arr = [5,4,3,2,1]

insertionSort(my_arr)

print(my_arr)



