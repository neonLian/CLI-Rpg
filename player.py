import random as r
import util as u
from weapon import Weapon, weapon_list

class Player():
	def __init__(self, conn, cause, money, name="Player"):
		self.HP = 400
		self.name = name
		self.conn = conn
		self.password = ""
		self.cause = cause
		self.currency = money
		self.money = 0
		self.mana = 50
		self.weapons = {}
		self.level = 1
		self.multiplier = 1.0
		self.kills = 0
		self.effects = []
		self.xp = 0

	def reset(self):
		self.HP = 400 * self.multiplier
		self.effects = []
		self.mana = 50

	def do_effects(self):
		self.mana += 5
		# Burning
		if "burning" in self.effects:
			u.s2c(self.conn, "You have taken burn damage.\n")
			self.HP -= r.randint(5, 10)
		if "bleeding" in self.effects:
			u.s2c(self.conn, "You have taken bleed damage.\n")
			self.HP -= r.randint(15, 30)

	def add_weapon(self, weapon):
		for w in weapon_list:
			if w.name == weapon:
				self.weapons[weapon] = w(self)
	
	def level_up(self):
		self.level += 1
		self.multiplier = 1 + ((self.level-1) / 10)
		self.HP = 400 * self.multiplier

	def __str__(self):
		return "%s [Lvl %d], HP: %d, Mana: %d" % (self.name, self.level, self.HP, self.mana)
	
