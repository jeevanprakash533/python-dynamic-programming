n=int(input("Enter number of rows"))
ans=[]
for i in range(n):
    row=[0]*(i+1)
    row[0]=1
    row[i]=1
    for j in range(1,i):
        row[j]=ans[i-1][j-1]+ans[i-1][j]
    ans.append(row)
print(ans)