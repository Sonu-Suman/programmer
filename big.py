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