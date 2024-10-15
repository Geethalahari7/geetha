class parent1:
	def first(self):
		print("parent1")
class parent2:
	def second(self):
		print("parent2")
class child(parent1,parent2):
	def third(self):
		print("child")
obj=child()
obj.first()
obj.second()
obj.third()
