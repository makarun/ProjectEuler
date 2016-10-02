'''
	Finding sum of prime number below 2000000 with Sieve of Eratosthenes

'''
numbers = []
sum_of_primes = 0

for i in range(0, 2000000):
	numbers.append(0)

#od indeksu 2 do końca listy

for i in range(2, len(numbers)):
	if numbers[i] == 0:
		y = i*2
		while y <= len(numbers)-1:
			numbers[y] = 1
			y += i

for i in range(2,len(numbers)):
	if numbers[i] == 0:
		sum_of_primes += i

print(sum_of_primes)