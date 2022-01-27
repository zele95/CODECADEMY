def sum_of_prime_factors(n):
    # returns a sum of all the prime factors of n
    prime_factors = []
    for i in range(2,n+1):
        if n%i == 0:
            prime = True
            for j in range(2,i):
                if i%j == 0:
                    prime = False  
            if prime == True:
                prime_factors.append(i)
        else:
            pass
    return sum(prime_factors)



print(sum_of_prime_factors(91))