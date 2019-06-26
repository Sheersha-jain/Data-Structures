def SieveOfEratosthenes(n):
    prime = [True for i in range(n)]
    p=2
    while(p*p <= n):
        if prime[p] is True:
            for i in range(p*p, n, p):
                prime[i] = False
        p +=1

    for p in range(2, n):
        if prime[p]:
            print(p)

SieveOfEratosthenes(50)