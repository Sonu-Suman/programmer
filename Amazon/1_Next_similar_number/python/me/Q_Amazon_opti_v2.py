from itertools import permutations
import math
import time


t1 = time.time()
class Solution:
    # @param A : string
    # @return a strings
    def jumpSearch(self, l, val, ma):
        prev=0
        step = ma*2
        if int(''.join(list(l[step])))==int(''.join(val)):
            for i in list(l[step:]):
                if int(''.join(list(i)))>int(''.join(val)):
                    return ''.join(list(i))
        elif int(''.join(list(l[prev])))==int(''.join(val)):
            for i in list(l[prev:]):
                if int(''.join(list(i)))>int(''.join(val)):
                    return ''.join(list(i))
            # return ''.join(list(l[step])), ''.join(list(l[prev])), ''.join(val)
        else:
            if int(''.join(list(l[step]))) > int(''.join(val)) > int(''.join(list(l[prev]))):
                return self.search(l[prev:step], val, 0, len(l[prev:step])-1)
            else:
                return self.jumpSearch(l, val, step)


    def search(self, l, A, mi, ma):

        mid = math.floor((mi+ma)/2)
        try:
            if int(''.join(list(l[mid])))==int(''.join(A)):
                for i in list(l[mid:ma+1]):
                    if int(''.join(list(i)))>int(''.join(A)):
                        return ''.join(list(i))
                else:
                    return -1
            else:
                if int(''.join(list(l[mid])))>int(''.join(A)):
                    return self.search(l, A, 0, mid)
                else:
                    return self.search(l, A, mid, ma)
        except:
            return -1


    def solve(self, A):
        if len(A)<2:
            return -1
        A = list(A)
        l = list(permutations(A, len(A)))
        l.sort()
        mi = 0

        return self.jumpSearch(l , A, 40)


t2 = time.time()


so = Solution()
print(so.solve('7409488012'))