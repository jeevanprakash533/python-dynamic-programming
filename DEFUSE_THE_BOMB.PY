l=[5,7,1,4]
k=3
ans=[]
for i in range(len(l)):
    sum=0
    for j in range(1,k+1):
        if i+j<len(l):
            sum+=l[j]
        else:
            p=abs(i+j)-len(l)
            sum+=l[p]
    ans.append(sum)
print(ans)