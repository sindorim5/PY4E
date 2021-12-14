class PartyAnimal:
	x = 0

	def __init__(self):
		print('I am constructed')

	def party(self):
		self.x = self.x + 1
		print("So far", self.x)

	def __del__(self):
		print('I am destructed', self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print("Type1", type(an))
print("Dir1 ", dir(an))

an = 42

print("Type2", type(an))
print("Dir2 ", dir(an))
