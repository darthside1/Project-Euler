def largest_prime_factor(n):

    largest_factor = 0

    while n % 2 == 0:
        largest_factor = 2
        n /= 2
    
    while n % 3 == 0:
        largest_factor = 3
        n /= 3
    
    for i in range(5, int(n **(1/2) + 1), 6):

        while n % i == 0:
            largest_factor = i
            n /= i

        while n % (i + 2) == 0:
            maxPrime = i + 2
            n /= (i + 2)

    if n > 4:
        largest_factor = n
    
    return largest_factor


print()

number = 600851475143
print(largest_prime_factor(13195))
print(largest_prime_factor(number))
print(largest_prime_factor())


print()