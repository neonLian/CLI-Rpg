import random as r
class Player():
	def __init__(self):
		self.HP = 100
		self.damage = 10
		#name = player till the player gives its name
		self.name = "Player"
		self.mana = 20
		self.weapons = []
		self.level = 1
		#player state could be used for is burning or if you have an effect like a potion or spell
		self.effects = []
	def do_effects(self):
		# Burning
		if "burning" in self.effects:
			self.HP -= r.randint(5, 10)
	
	
	
