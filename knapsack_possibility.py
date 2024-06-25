# knapsack problem
val=[200,150,50]
weight=[10,20,30]
capacity=50
def knap(val,weight,capacity,n):
    if n==0 or capacity==0:
        return 0
    if weight[n-1]>capacity:
        knap(val,weight,capacity,n-1)
    else:
        return max(val[n-1]+knap(val,weight,capacity-weight[n-1],n-1),knap(val,weight,capacity,n-1))
n=len(val)
knap(val,weight,capacity,n)
print(knap(val,weight,capacity,n))