# This solution based upon data structure method

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