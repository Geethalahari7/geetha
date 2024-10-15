class parent:
	def first(self):
		print('This is parent Class')
class child1(parent):
	def second(self):
		print('This is child1 class')
class child2(child1):
	def third(self):
		print('This is child2 class')
obj=child2()
obj.first()
obj.second()
obj.third()
