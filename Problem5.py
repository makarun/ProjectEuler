"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

number = 0

while True:
	for i in range(1,21):
		if number%i != 0:
			number += 10
	print(number)
	break