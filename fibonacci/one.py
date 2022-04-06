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