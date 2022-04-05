from itertools import permutations
import math

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        if len(A)<2:
            return -1
        A = list(A)
        l = list(permutations(A, len(A)))
        l.sort()
        mi = 0

        return self.search(l, A, mi, len(l)-1)


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


s = Solution()
A = '740948'
print(s.solve(A))