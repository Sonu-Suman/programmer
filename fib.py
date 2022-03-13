# This is the first Approach and it's take lots of time for finding result.
# This is based upon Reccurssion methode

# 1)
class Sol:
    def fib_2(self, n):
        assert n>=0 and int(n) == n, 'Please enter the postive integer input.'

        if n in [1, 2]:
            result = 1
        else:
            result = self.fib_2(n-1) + self.fib_2(n-2)

        return result


s1 = Sol()
print(s1.fib_2(40))
# This takes around 40-60 sec for finding result

# 2).

def fib(n):
    if n<=1:
        return n

    return fib(n-1)+fib(n-2)


# This is the Seocnd Approach and it's takes much less time
# This solution based upon Dynamic Programming data structure method

# 1).
class Solution:
    def fib(self, n, memo):
        assert n>=0 and int(n) == n, 'Please enter the postive integer input.'

        if memo[n] is not None:
            return memo[n]

        if n in [1, 2]:
            result = 1
        else:
            result = self.fib(n-1, memo) + self.fib(n-2, memo)

        memo[n] = result

        return result

    def fib_memo(self, n):
        memo = [None]*(n+1)
        return self.fib(n, memo)


s = Solution()
print(s.fib_memo(40))


# 2).

def fib(n):
    f = {}
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1]+f[i-2]

    return f[n]


# For Memory limit

def solve(A):
    fib = [0] * 3
    if A<=1:
        fib[0] = 0
        fib[1] = 1
        return fib[A]
    else:
        fib[0] = 0
        fib[1] = 1
        
        i = 1
        while i<=A:
            fib[0] = fib[1]
            fib[1] = fib[2]
            fib[2] = (fib[0]+fib[1])
            i +=1
        
        return fib[2]

print(solve(100000))