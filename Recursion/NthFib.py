#first method
#time o(2^n)
#space o(n)
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#second method
#memoization/cashing
#o(n) time and space
def fib(n):
    memo={}
    if n == 1:
        memo[1] = 0
        return memp[1]
    elif n == 2:
        memo[2] =  1
        return memo[2]
    else:
        if n in memo:
            return memo[n]
        else:
            memo[n] = fib(n-1) + fib(n-2)
#3rd method
#iterative solution
#o(n) time o(1) space
def fib(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter+=1
    return lastTwo[1] if n > 1 else lastTwo[0]

