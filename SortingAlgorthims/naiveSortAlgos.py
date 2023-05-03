#Basic brute force algorithims for sorting integer arrays in acending and decending order


arr = [10,2,4,45,42,6,2,1,7]

def acendingSort(arr):
    newArr = []
    smallest = sum(arr)
    for i in range(len(arr)):
        temp = arr[i]
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                temp = arr[j]
        if temp < smallest:
            arr.pop(temp)
            newArr.append(temp)
            smallest = temp
    return newArr


print(acendingSort(arr))








def decendingSort(arr):
    largets = 0
    newArr = []
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            
            if arr[i] > largest:
                largest = arr[i]
            arr.remove(arr[i])
        newArr +=[largest]
    return newArr
