def tower(n,s,e,d):
    # base condition
    if n==1:
        print("move",n,"from",s,"to",d)
        return
    # source to destination to extra
    tower(n-1,s,d,e)
    print("move",n,"from",s,"to",d)
    # extra to destination through source
    tower(n-1,e,s,d)
n=5
tower(n,"source","extra","destinaton")

