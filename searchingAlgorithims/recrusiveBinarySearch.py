# a binary search function which works on a sorted array.
# it works by recursively calling itself on a increasingly smaller list
# the a slice of the array from the upper and lower bounds is input as the arr parameter for the recursive function call.






def binsearch2(arr, target):
    split = round(len(arr)/2)
    if arr[split] == target:
        return f"target value {target} found at indx {split}"
    if arr[split] > target:
        binsearch2(arr[0: split], target)
    if arr[split] < target:
        binsearch2(arr[split: len(arr)], target)

print(binsearch2([1,2,3,4,5,6,7,8,9,10], 3))
    
