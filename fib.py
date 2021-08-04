# This is the first Approach and it's take lots of time for finding result.
# This is based upon Reccurssion methode

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


# This is the Seocnd Approach and it's takes much less time
# This solution based upon Dynamic data structure method

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