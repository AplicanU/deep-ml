def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	dot_prod = []

	if len(a) == 0:
		return -1

	for n in range(len(a)):
		if len(a[n]) != len(b):
			return -1
		add = 0
		for m in range(len(b)):
			prod = a[n][m] * b[m]
			add += prod
		dot_prod.append(add)
	
	return dot_prod