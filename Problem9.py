for x in range(1,1000):
	for y in range(x,1000):
		for z in range(y,1000):
			if x+y+z == 1000:
				if (x**2 + y**2) == z**2:
					print(x*y*z)
