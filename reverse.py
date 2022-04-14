# How to reverse array

def reverse(arr):
    for i in range(int(len(arr)/2)):
        other = len(arr)-i-1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp

    print(arr)


reverse([12, 23, 34, 45, 56, 67, 78, 89])


# This is the sortest method for rversing array.

print(reverse([12, 23, 34, 45, 56, 67, 78, 89]))