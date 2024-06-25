import sys
sys.setrecursionlimit(10000)
def fun(n):
    print(n)
    fun(n+1)
fun(1)