# For non repeative minimum element

class Solution:
    # @param A : string
    # @return a strings
    def search(self, A):
        A = list(A)
        A1 = A.copy()
        A2 = A.copy()

        A1.sort(reverse=True)
        A2.sort(reverse=False)

        if int(''.join(A)) == int(''.join(A1)):
            return -1
        elif int(''.join(A)) == int(''.join(A2)):
            A[-1], A[-2] = A[-2], A[-1]
            return ''.join(A)
        else:
            m = A[1:]
            m.sort()
            m0 = m[0]
            m1 = m[1]
            ind0 = A.index(m0)
            ind1 = A.index(m1)
            A[ind0], A[ind1] = m1, m0
            A0 = A[ind0 + 1:]
            A0.sort()
            A[ind0 + 1:] = A0
            return ''.join(A)


s = Solution()

print(s.search('218765'))