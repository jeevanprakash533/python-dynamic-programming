# memoization method in dynamic programming
n = int(input())
c = 0
def fib(n,memo):
    global c
    c += 1
    if memo[n]:
        return memo[n]

    if n<=1:
        return n
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
memo = [0]*(n+1)
print(fib(n,memo))
print(c)

    