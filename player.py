import random as r
class Player():
	def __init__(self, name="Player"):
		self.HP = 100
		#name = player till the player gives its name
		self.name = name
		self.mana = 50
		self.weapons = {}
		self.level = 1
		#player state could be used for is burning or if you have an effect like a potion or spell
		self.effects = []
	def do_effects(self):
		self.mana += 5
		# Burning
		if "burning" in self.effects:
			self.HP -= r.randint(5, 10)
	def add_weapon(self, weapon):
		self.weapons[weapon.name] = weapon
	
	def __str__(self):
		return "%s [Lvl %d], HP: %d, Mana: %d" % (self.name, self.level, self.HP, self.mana)
	
