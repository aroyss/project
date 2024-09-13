def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    

for n in range(1,100):
    print(f"n={n}, n!={fact(n)}")