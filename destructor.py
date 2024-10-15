class cons:
	def __init__(self):
		self.greet="HI"
	def display(self):
		print(self.greet)
	def __del__(self):
		print("Object Destroyer")
obj=cons()
obj.display()
print(obj) #prints object address
del obj
