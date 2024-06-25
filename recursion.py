def func(n):
    if n<=1:
        print(1)
    else:
        func(n-1)
        print(n,"-hi")
func(4)