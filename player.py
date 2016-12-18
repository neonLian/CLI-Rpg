import random as r
class Player():
	def __init__(self, name="Player"):
		self.HP = 400
		#name = player till the player gives its name
		self.name = name
		self.mana = 50
		self.weapons = {}
		self.level = 1
		self.multiplier = 1.0
		self.effects = []

	def do_effects(self):
		self.mana += 5
		# Burning
		if "burning" in self.effects:
			print(self.name + " has taken burn damage.\n")
			self.HP -= r.randint(5, 10)
	def add_weapon(self, weapon):
		self.weapons[weapon.name] = weapon
	
	def level_up(self):
		self.level += 1
		self.multiplier = 1 + ((self.level-1) / 10)
		self.HP *= self.multiplier

	def __str__(self):
		return "%s [Lvl %d], HP: %d, Mana: %d" % (self.name, self.level, self.HP, self.mana)
	
