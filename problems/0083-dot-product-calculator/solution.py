import numpy as np

def calculate_dot_product(vec1, vec2):
	"""
	Calculate the dot product of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The dot product of the two vectors.
	"""

	# manual implementation
	result = 0
	for i in range(len(vec1)):
		prod = vec1[i] * vec2[i]
		result += prod
	
	return result

	'''
	return np.dot(vec1, vec2)
	'''