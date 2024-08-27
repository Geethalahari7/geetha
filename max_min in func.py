def max_min(numbers):
	largest=max(numbers)
	smallest=min(numbers)
	return largest,smallest
numbers=[1,6,8,6,5,4]
largest, smallest=max_min(numbers)
print(largest)
print(smallest)
