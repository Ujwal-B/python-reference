def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def insert (array, item):
    size = len(array)
    if size == 0:
        array.append(item)
    else:
        array.append(item)
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def delete (array, item):
    size = len(array)
    i = 0
    for i in range (0, size):
        if item == array[i]:
            break
    array[i], array[size-1] = array[size-1], array[i]
    array.remove(item)
    for i in range((size//2)-1, -1, -1):
        heapify(array, len(array), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max heap array: ", arr)

delete(arr, 4)
print("Max heap array: ", arr)

