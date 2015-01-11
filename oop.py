class Animal:
	def __init__(self,name,color,age,size ):
		self.name=name
		self.age=age
		self.color=color
		self.size=size
		
	def print_all(self):
		print(self.name)
		print(self.color)
		print(self.age)
		print(self.size)
	def eat(self,food):
		print(self.name,"is eating",food)
	def sleep(self):
		print(self.name,"is sleeping")

dog = Animal(name="max",color="black",age=4,size="huge")
cat = Animal(name="min",color="white",age=2,size="tiny")

dog.print_all()
dog.eat(food="pizza")
dog.sleep()
print("##############")
cat.print_all()
cat.eat(food="fish")
cat.sleep()

