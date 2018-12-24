"""
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt
either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a
dog or a cat (receive the oldest animal of that type). They cannot select which specific animal they would like.
Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and 
dequeueCat. You may use the built-in LinkedList data structure.
"""
class Animal:
	def __init__(self, animalName=None, animalType=None):
		self.animalName = animalName
		self.animalType = animalType
		self.next = None
		self.timestamp = 0
		
class AnimalShelter:
	def __init__(self):
		self.headCat = None
		self.tailCat = None
		self.headDog = None
		self.tailDog = None
		self.order = 0

	def enqueue(self, animalName, animalType):
		self.order += 1 
		newAnimal = Animal(animalName, animalType)
		newAnimal.timestamp = self.order

		if animalType == 'cat':
			if not self.headCat:
				self.headCat = newAnimal
			if self.tailCat:
				self.tailCat.next = newAnimal
			self.tailCat = newAnimal

		elif animalType == 'dog':
			if not self.headDog:
				self.headDog = newAnimal
			if self.tailDog:
				self.tailDog.next = newAnimal
			self.tailDog = newAnimal

	def dequeueCat(self):
		if self.headCat:
			newAnimal = self.headCat
			self.headCat = newAnimal.next
			return str(newAnimal.animalName)
		else:
			return "No cat left!"

	def dequeueDog(self):
		if self.headDog:
			newAnimal = self.headDog
			self.headDog = newAnimal.next
			return str(newAnimal.animalName)
		else:
			return "No dog left!"
			
	def dequeueAny(self):
		if self.headCat and not self.headDog:
			return self.dequeueCat()
		elif not self.headCat and self.headDog:
			return self.dequeueDog()
		elif self.headCat:
			if self.headCat.timestamp < self.headDog.timestamp:
				return self.dequeueCat()
			else:
				return self.dequeueDog()
		else:
			return "No animal left!"