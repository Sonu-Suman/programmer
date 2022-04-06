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