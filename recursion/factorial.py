def factorial(n):
    assert n >= 0
    if n < 2:
        print("factorial is 1")
    else:
        return n * factorial(n-1)

def fib( n ):
    #assert n <= 1, "Fibonacci not defined for n < 1."
    if n == 1 :
        return 1
    else :
        while(n>0):
            return fib(n - 1) + fib(n - 2)

fib(7)