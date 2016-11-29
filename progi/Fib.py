__author__ = 'student'
def fibon(n):
    Fib = [0,1] + [0]*(n)
    for i in range (2, n+1):
        Fib[i] = Fib[i-1] + Fib[i-2]
        #print(Fib[i])
    print(Fib[n])
    return Fib[n]

fibon(10)