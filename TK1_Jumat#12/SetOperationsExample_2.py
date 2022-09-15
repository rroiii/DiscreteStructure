def func():
    N = int(input("Input a number you want to check whether it is prime or not."))
    for i in [x+1 for x in range(N)]:
        if N % i==0 and (i!=1 and i!=N):
            return False
    return True
print (func())





