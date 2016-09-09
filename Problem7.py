"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


wybitnie nie optymalne rozwiązanie : /

z wykorzystaniem Sita Eratostenesa

"""

list_of_primes = []
for i in range (2,150000):
	list_of_primes.append(i)

for i in list_of_primes:
	if i != 0:
		for y in range(i, len(list_of_primes)):
			if list_of_primes[y]%i == 0:
				list_of_primes[y] = 0

while 0 in list_of_primes:
	list_of_primes.remove(0)

#print(len(list_of_primes))
print(list_of_primes[10000])