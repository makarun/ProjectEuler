"""

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

numbers = []

for i in range (100, 999):
	for y in range (100, 999):
		product = i*y
		str_product = str(product)
		if str_product[0] == str_product[-1] and str_product[1] == str_product[-2] and str_product[2] == str_product[-3]:
			numbers.append(product)

print(max(numbers))	
