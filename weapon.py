import random as r
import util as u
class Weapon():
	def __init__(self, player, dmg, mana=0, effects=[],price = 0):
		self.name = type(self).name
		self.damage = dmg
		self.mana_cost = mana
		self.effects = effects
		self.buff = dmg <= 0
		self.player = player
		self.price = price
	
	def special(self, player):
		pass
	
	def attack(self, player):
		self.special(player)
		if self.player.mana >= self.mana_cost:
			player.HP -= self.damage * self.player.multiplier + r.randint(-5, 5)
			self.player.mana -= self.mana_cost
		else:
			u.s2c(self.player.conn, "Need %d mana to use %s" % (self.mana_cost, self.name))
		for effect in self.effects:
			if not effect in player.effects:
				player.effects.append(effect)
	def desc(self):
		return "%s deals %d damage to a player for %d mana." % (self.name, self.damage, self.mana_cost)

class AngryPiranha(Weapon):
	name = "Angry Piranha"
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=60, effects=["bleeding"],price = 180)
	def desc(self):
		return Weapon.desc()  

class AntiFireExtinguisher(Weapon):
	name = 'Anti-Fire Extinguisher'
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=100, mana=40, effects=["burning"],price = 210)

class EdibleRainbow(Weapon):
	name = 'Edible Rainbow'
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=-60, mana=30,price = 50)
	
	def special(self, player):
		self.player.effects = []

class Manapua(Weapon):
	name = 'Manapua'
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=0,price = 40)
	
	def special(self, player):
		player.mana += 50

class Matchmaker(Weapon):
	name = 'Matchmaker'
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=75, mana=25, effects=["burning"],price = 190)

class axe(Weapon):
	name = "Executioner's Axe"
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=40,price = 150)
	
	def attack(self, player):
		if self.damage * 4 >= player.HP:
			player.HP = -100
		else:
			player.HP -= self.damage
class club(Weapon):
	name = "Club"
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=65,price = 60)

class spear(Weapon):
	name = "Spear"
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=70,price = 80)

# i was thinking you could load the bow with arows that have efects thats why the dmg is so low
class Bow(Weapon):
	
	name = "Bow"
	def __init__(self, player):
		Weapon.__init__(self,player,dmg=50,price = 70)

	def special(self, player):
		player.mana -= 10
		self.player.mana += 10

class Zap(Weapon):
	name = "Zap"
	def __init__(self, player):
		Weapon.__init__(self, player, dmg=25,price = 75)
	
	def special(self, player):
		player.mana -= 30
weapon_list = [AngryPiranha, AntiFireExtinguisher, Matchmaker, axe, club, spear, Bow, Zap]
