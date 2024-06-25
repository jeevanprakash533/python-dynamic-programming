n = int(input())
i = 2
ans = 0
def prime(i,n):
    if n%i==0:
        return "Not prime"
        # print("Not a prime number")
    elif i==n-1:
        return "Prime"
        # print("Prime")
    else:
        return prime(i+1,n)
        # print(i+1,n)
print(prime(i,n))  