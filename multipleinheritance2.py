class parent1:
	def first(self):
		print("parent1")
class parent2(parent1):
	def second(self):
		print("parent2")
class parent3(parent1):
	def third(self):
		print("parent3")
class child(parent2,parent3):
	def four(self):
		print("child")
obj=child()
obj.first()
obj.second()
obj.third()
obj.four()
