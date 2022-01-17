class Number:
	def __init__(self,value):
		self.value = value
	
	def __str__(self):
		return str(self.value)
	
	def is_reducible(self):
		return False


class Boolean:
	def __init__(self,value):
		self.value = value

	def __str__(self):
		return str(self.value)
	
	def is_reducible(self):
		return False


class Variable:
	def __init__(self,name):
		self.name = name
	
	def is_reducible(self):
		return True
	
	def __str__(self):
		return str(self.name)
	
	def reduce(self,environment):
		return environment[self.name]


class Add:
	def __init__(self,left,right):
		self.left = left
		self.right = right
	
	def __str__(self):
		return f"{self.left} + {self.right}"
	
	def is_reducible(self):
		return True
	
	def reduce(self,environment):
		if self.left.is_reducible():
			return Add(self.left.reduce(environment),self.right)
		elif self.right.is_reducible():
			return Add(self.left,self.right.reduce(environment))
		else:
			return Number(self.left.value+self.right.value)

class Multiply:
	def __init__(self,left,right):
		self.left = left
		self.right = right
	
	def __str__(self):
		return f"{self.left}*{self.right}"
	
	def is_reducible(self):
		return True
	
	def reduce(self,environment):
		if self.left.is_reducible():
			return Multiply(self.left.reduce(environment),self.right)
		elif self.right.is_reducible():
			return Multiply(self.left,self.right.reduce(environment))
		else:
			return Number(self.left.value*self.right.value)


class LessThan:
	def __init__(self,left,right):
		self.left = left
		self.right = right

	def __str__(self):
		return f"{self.left}<{self.right}"

	def is_reducible(self):
		return True

	def reduce(self,environment):
		if self.left.is_reducible():
			return LessThan(self.left.reduce(environment),self.right)
		elif self.right.is_reducible():
			return LessThan(self.left,self.right.reduce(environment))
		else:
			return Boolean(self.left.value<self.right.value)



class Machine:
	def __init__(self,expression,environment):
		self.expression = expression
		self.environment = environment

	def step(self):
		self.expression = self.expression.reduce(self.environment)

	def run(self):
		while self.expression.is_reducible():
			print(self.expression)
			self.step()
		print(self.expression)





expr = LessThan(Number(5),Add(Number(2),Number(2)))
machine = Machine(Add(Variable("a"),Variable("b")),{"a":Number(39),"b":Number(4)})
machine.run()
