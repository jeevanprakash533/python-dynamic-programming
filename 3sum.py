l=[1,2,3,4,5,6,7,8]
target=11
ans=[]
result=[]
# for i in range(0,len(l)-1):
#     for j in range(i+1,len(l)-1):
#         ans=[]
#         for k in range(j+1,len(l)):
#             if l[i]+l[j]+l[k]==target:
#                 ans.append(i)
#                 ans.append(j)
#                 ans.append(k)
#                 result.append(ans)
# print(result)
i=0
while i<len(l)-2:
    j=i+1
    k=len(l)-1
    while j<k:
        ans=[]
        if l[i]+l[j]+l[k]==target:
            ans.append(i)
            ans.append(j)
            ans.append(k)
            result.append(ans)
            k-=1
            continue
        elif l[i]+l[j]+l[k]<target:
            j+=1
        else:
            k-=1
    i+=1
print(result)

