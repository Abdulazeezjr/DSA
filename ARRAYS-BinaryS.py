def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(7))
#bubble sort
def bubble_sort():
    my_array = [64, 34, 25, 12, 22, 11, 90, 5]
    for i in range(len(my_array)-1):
        print(my_array)
        for j in range(len(my_array)-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
    print(my_array)
#selection sort
def selection_sort():
    sel_array = [64, 34, 25, 12, 22, 11, 90, 5]
    temp = 0
    for i in range(len(sel_array)-1):
        temp = sel_array[i]
        print(sel_array)
        for j in range(i+1,len(sel_array)):
            if sel_array[j] < temp:  
                temp = sel_array[j]
                sel_array[j] = sel_array[i]
                sel_array[i] = temp
    return sel_array
# print(selection_sort())

#quick sort 
def quick_sort(arr):
    if len(arr) < 1:
        return arr
    print(arr)
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort([64, 34,2,25, 12, 22, 11, 90, 5,1]))

def count_sort():
    arr = [64, 34,2,25, 12, 22, 11, 90, 5,1]
    maxi = max(arr)
    # use the largest number to create the number of zero's
    count = [0] * (maxi + 1)
    # starting from  zero count how many times a number appear
    for num in arr:
        count[num] += 1
    # now if their count is != 0 add them to the output starting from 0-64 
    # a long ass loop
    output =[]
    for i in range(len(count)):
        output.extend([i] * count[i])
    return output

# radix sort
def radix_sort():
    myArray = [170, 45, 75, 90, 802, 24, 2, 66]
    radixArray = [[] for i in range(10)]
    max_value = max(myArray)
    exp = 1
    while max_value // exp > 0:
        while len(myArray) > 0:
            val = myArray.pop()
            radiindex = (val//exp) % 10
            radixArray[radiindex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                myArray.append(val)
                
        exp *= 10
    return myArray

# merge sort
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    sortedleft = mergesort(left)
    sortedright = mergesort(right)
    return merge(sortedleft, sortedright)

def merge(left, right):
    result = []
    i,j = 0,0
    print(left, right)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
        
mergesort([170, 45, 75, 90, 5,3, 24, 2, 66])

def linear_search(arr,tar):
    if len(arr) < 1:
        return -1
    for i in range(len(arr)):
        if arr[i] == tar:
            return i
    return -1
print(linear_search([170, 45, 75, 90, 5,3, 24, 2, 66], 2))

def binary_search(arr, tar):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == tar:
            return mid
        if arr[mid] < tar:
            left += 1
        else:
            right -= 1
    return -1
binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 5)