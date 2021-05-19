# Finding the biggest number in array not uisng max function

# This is only applicable for small array and list:
# This is not for big array

lst = []
i = 0

while i < 3:
    num = int(input("Enter your number for list: "))
    lst.append(num)
    i += 1

print(lst)

if lst[0] > lst[1]:
    if lst[2] > lst[0]:
        print(lst[2], " is the biggest number in the list!")
    else:
        print(lst[0], " is the biggest number in the list!")
else:
    if lst[1] > lst[2]:
        print(lst[1], " is the biggest number in this list")
    else:
        print(lst[2], " is the biggest number in the list")


# This is also applicable for big array



def findbiggestNumber(arr):
    biggestnumber = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > biggestnumber:
            biggestnumber = arr[i]

    print('This is the biggest number in your array: ', biggestnumber)

findbiggestNumber([43, -23, 23, 95, 234, 230, 809])