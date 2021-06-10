# Convert the string "123" into 123, without using the built-api `int()`

s = '123'


def strToInt(s):
    j = 0
    for i in s:
        for k in range(10):
            if str(k) == i:
                j = j*10 + k
    return j


print(strToInt(s))