def SieveofEratosthenes(num):
    primes = [True for i in range(num + 1)]

    p = 2
    while (p * p <= num):

        if (primes[p] == True):

            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    for p in range(2, num + 1):
        if primes[p]:
            print(p)

num = int(input("Enter the number: "))
print("Following are the prime numbers smaller"),
print("than or equal to", num)
SieveofEratosthenes(num)
     