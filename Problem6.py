sum_of_squeres = 0
squere_of_sums = 0

for i in range(1,101):
	sum_of_squeres += i**2
	squere_of_sums += i

print(squere_of_sums**2 - sum_of_squeres)