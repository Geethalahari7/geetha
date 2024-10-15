class parent:
	def first(self):
		print('This is parent Class')
class child(parent):
	def second(self):
		print('This is child class')
obj=child()
obj.first()
obj.second()
