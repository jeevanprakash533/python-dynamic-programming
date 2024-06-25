n = int(input())
ans = 0
def reverse(n,ans):
    if n==0:
        return ans
    else:
        rem = n%10
        ans = ans*10+rem
        return reverse(n//10,ans)
print(reverse(n,ans))
# print (ans)